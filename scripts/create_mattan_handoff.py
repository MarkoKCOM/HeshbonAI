#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path('/root/.openclaw/agents/sales-heshbonai/workspace')
TARGETS = ROOT / 'prospects/targets-usa.md'
OUTREACH = ROOT / 'memory/outreach-log.md'
OUTDIR = ROOT / 'handoffs' / 'mattan'
OUTDIR.mkdir(parents=True, exist_ok=True)
TODAY = '2026-03-27'


def clean_value(v: str) -> str:
    if v is None:
        return ''
    return v.strip().replace('—', '-')


def normalize_email(v: str) -> str:
    v = clean_value(v)
    if not v:
        return ''
    low = v.lower()
    if '[email protected]' in low or 'contact form' in low or 'contact via website' in low or 'use contact form' in low or 'call to request' in low:
        return ''
    return v


def firm_norm(name: str) -> str:
    name = (name or '').lower()
    name = name.replace('&', 'and')
    name = re.sub(r'\([^)]*\)', '', name)
    name = re.sub(r'[^a-z0-9]+', '', name)
    return name


def parse_targets():
    text = TARGETS.read_text()
    lines = text.splitlines()
    prospects = []
    current_section = ''
    current = None

    def finalize(obj):
        if not obj:
            return
        obj['email'] = normalize_email(obj.get('email', ''))
        prospects.append(obj)

    for line in lines:
        m_section = re.match(r'^##\s+(.*)$', line)
        if m_section and not line.startswith('###'):
            current_section = m_section.group(1).strip()
            continue

        m_prospect = re.match(r'^###\s+(\d+)\.\s+(.*)$', line)
        if m_prospect:
            finalize(current)
            current = {
                'prospect_number': int(m_prospect.group(1)),
                'firm_name': clean_value(m_prospect.group(2)),
                'section': current_section,
                'location': '',
                'website': '',
                'size': '',
                'email': '',
                'phone': '',
                'specialization': '',
                'why_target': '',
            }
            continue

        if current and line.startswith('- **'):
            m_field = re.match(r'^- \*\*(.+?):\*\*\s*(.*)$', line)
            if m_field:
                field = m_field.group(1).strip().lower()
                value = clean_value(m_field.group(2))
                keymap = {
                    'location': 'location',
                    'website': 'website',
                    'size': 'size',
                    'email': 'email',
                    'phone': 'phone',
                    'specialization': 'specialization',
                    'why target': 'why_target',
                }
                if field in keymap:
                    current[keymap[field]] = value

    finalize(current)

    # Fill confirmed emails from markdown tables keyed by prospect number.
    table_email_map = {}
    for line in lines:
        m_row = re.match(r'^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$', line)
        if m_row:
            num = int(m_row.group(1))
            email = normalize_email(m_row.group(3))
            if email:
                table_email_map[num] = email

    for p in prospects:
        if not p['email'] and p['prospect_number'] in table_email_map:
            p['email'] = table_email_map[p['prospect_number']]

    return prospects


def parse_outreach():
    text = OUTREACH.read_text().splitlines()
    initial = []
    follow2 = []
    current_section = ''
    current_date = ''
    headers = []

    for line in text:
        m_heading = re.match(r'^##\s+(\d{4}-\d{2}-\d{2})\s+-\s+(.*)$', line)
        if m_heading:
            current_date = m_heading.group(1)
            current_section = m_heading.group(2).strip()
            headers = []
            continue

        if line.startswith('| # |'):
            headers = [h.strip().lower() for h in line.strip('|').split('|')]
            continue

        if headers and line.startswith('|') and not line.startswith('|---'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) != len(headers):
                continue
            row = dict(zip(headers, cells))
            firm = row.get('firm', '')
            status = row.get('status', '')
            if not firm:
                continue

            if 'usa campaign' in current_section.lower() and 'follow-up' not in current_section.lower():
                if 'contacted' in status.lower() and 'test' not in status.lower():
                    initial.append({
                        'firm': firm,
                        'email': row.get('email', ''),
                        'sequence': row.get('sequence', row.get('seq', '')),
                        'email1_subject': row.get('subject', ''),
                        'first_contact_date': current_date,
                        'contact_wave': current_section,
                    })

            if 'email 2 follow-ups' in current_section.lower() and status.lower() == 'sent':
                follow2.append({
                    'firm': firm,
                    'email2_sent_date': current_date,
                    'email2_subject': row.get('subject', ''),
                })

    return initial, follow2


def best_match(prospect_name, rows):
    pn = firm_norm(prospect_name)
    matches = []
    for row in rows:
        rn = firm_norm(row['firm'])
        if not rn:
            continue
        if pn == rn or pn in rn or rn in pn:
            score = min(len(pn), len(rn)) / max(len(pn), len(rn))
            matches.append((score, len(rn), row))
    if not matches:
        return None
    matches.sort(reverse=True)
    return matches[0][2]


def build_rows():
    prospects = parse_targets()
    initial, follow2 = parse_outreach()

    all_rows, reached_rows, cold_rows = [], [], []
    for p in prospects:
        init = best_match(p['firm_name'], initial)
        f2 = best_match(p['firm_name'], follow2)
        email = p['email']
        if init and normalize_email(init.get('email', '')):
            email = normalize_email(init['email'])
        contacted = bool(init)

        row = {
            'Prospect #': p['prospect_number'],
            'Firm Name': p['firm_name'],
            'Phone': p['phone'],
            'Email': email,
            'Email Status': 'Confirmed' if email else 'No public email / form only',
            'Location / Address on file': p['location'],
            'Website': p['website'],
            'Size': p['size'],
            'Specialization': p['specialization'],
            'Why Target': p['why_target'],
            'Source Section': p['section'],
            'Contacted Already': 'Yes' if contacted else 'No',
            'First Contact Date': init.get('first_contact_date', '') if init else '',
            'Contact Wave': init.get('contact_wave', '') if init else '',
            'Sequence': init.get('sequence', '') if init else '',
            'Email 1 Subject': init.get('email1_subject', '') if init else '',
            'Email 2 Sent Date': f2.get('email2_sent_date', '') if f2 else '',
            'Email 2 Subject': f2.get('email2_subject', '') if f2 else '',
        }
        all_rows.append(row)
        if contacted:
            reached_rows.append(row)
        else:
            cold_rows.append({
                'Prospect #': row['Prospect #'],
                'Firm Name': row['Firm Name'],
                'Phone': row['Phone'],
                'Email': row['Email'],
                'Email Status': row['Email Status'],
                'Location / Address on file': row['Location / Address on file'],
                'Website': row['Website'],
                'Size': row['Size'],
                'Specialization': row['Specialization'],
                'Why Target': row['Why Target'],
                'Source Section': row['Source Section'],
            })

    all_rows.sort(key=lambda r: int(r['Prospect #']))
    reached_rows.sort(key=lambda r: (r['First Contact Date'], int(r['Prospect #'])))
    cold_rows.sort(key=lambda r: (
        0 if r['Phone'] else 1,
        0 if r['Email'] else 1,
        int(r['Prospect #'])
    ))
    return all_rows, reached_rows, cold_rows


def write_csv(path: Path, rows, headers):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def col_letter(idx: int) -> str:
    s = ''
    while idx > 0:
        idx, rem = divmod(idx - 1, 26)
        s = chr(65 + rem) + s
    return s


def worksheet_xml(rows, headers):
    xml = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    xml.append('<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>')

    # header row
    xml.append('<row r="1">')
    for c_idx, header in enumerate(headers, start=1):
        cell = f'{col_letter(c_idx)}1'
        xml.append(f'<c r="{cell}" t="inlineStr"><is><t>{escape(str(header))}</t></is></c>')
    xml.append('</row>')

    for r_idx, row in enumerate(rows, start=2):
        xml.append(f'<row r="{r_idx}">')
        for c_idx, header in enumerate(headers, start=1):
            cell = f'{col_letter(c_idx)}{r_idx}'
            value = '' if row.get(header) is None else str(row.get(header))
            xml.append(f'<c r="{cell}" t="inlineStr"><is><t>{escape(value)}</t></is></c>')
        xml.append('</row>')
    xml.append('</sheetData></worksheet>')
    return ''.join(xml)


def workbook_xml(sheet_names):
    parts = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    parts.append('<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>')
    for i, name in enumerate(sheet_names, start=1):
        parts.append(f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>')
    parts.append('</sheets></workbook>')
    return ''.join(parts)


def workbook_rels_xml(sheet_count):
    parts = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    parts.append('<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">')
    for i in range(1, sheet_count + 1):
        parts.append(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>')
    parts.append('</Relationships>')
    return ''.join(parts)


def content_types_xml(sheet_count):
    parts = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    parts.append('<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">')
    parts.append('<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>')
    parts.append('<Default Extension="xml" ContentType="application/xml"/>')
    parts.append('<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>')
    for i in range(1, sheet_count + 1):
        parts.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
    parts.append('<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>')
    parts.append('<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>')
    parts.append('</Types>')
    return ''.join(parts)


def package_rels_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
            '</Relationships>')


def core_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<dc:creator>Closer</dc:creator>'
            '<cp:lastModifiedBy>Closer</cp:lastModifiedBy>'
            '<dcterms:created xsi:type="dcterms:W3CDTF">2026-03-27T08:30:00Z</dcterms:created>'
            '<dcterms:modified xsi:type="dcterms:W3CDTF">2026-03-27T08:30:00Z</dcterms:modified>'
            '</cp:coreProperties>')


def app_xml(sheet_names):
    titles = ''.join(f'<vt:lpstr>{escape(name)}</vt:lpstr>' for name in sheet_names)
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
            '<Application>OpenClaw</Application>'
            f'<TitlesOfParts><vt:vector size="{len(sheet_names)}" baseType="lpstr">{titles}</vt:vector></TitlesOfParts>'
            '</Properties>')


def write_xlsx(path: Path, sheets):
    sheet_names = [name for name, _, _ in sheets]
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('[Content_Types].xml', content_types_xml(len(sheets)))
        zf.writestr('_rels/.rels', package_rels_xml())
        zf.writestr('docProps/core.xml', core_xml())
        zf.writestr('docProps/app.xml', app_xml(sheet_names))
        zf.writestr('xl/workbook.xml', workbook_xml(sheet_names))
        zf.writestr('xl/_rels/workbook.xml.rels', workbook_rels_xml(len(sheets)))
        for i, (_, headers, rows) in enumerate(sheets, start=1):
            zf.writestr(f'xl/worksheets/sheet{i}.xml', worksheet_xml(rows, headers))


def main():
    all_rows, reached_rows, cold_rows = build_rows()

    all_headers = list(all_rows[0].keys())
    reached_headers = list(reached_rows[0].keys())
    cold_headers = list(cold_rows[0].keys())

    xlsx_path = OUTDIR / f'HeshbonAI_Mattan_USA_Prospects_{TODAY}.xlsx'
    reached_csv = OUTDIR / f'HeshbonAI_reached_out_USA_{TODAY}.csv'
    cold_csv = OUTDIR / f'HeshbonAI_cold_outreach_queue_USA_{TODAY}.csv'
    all_csv = OUTDIR / f'HeshbonAI_all_USA_prospects_{TODAY}.csv'

    write_csv(reached_csv, reached_rows, reached_headers)
    write_csv(cold_csv, cold_rows, cold_headers)
    write_csv(all_csv, all_rows, all_headers)
    write_xlsx(xlsx_path, [
        ('Reached Out', reached_headers, reached_rows),
        ('Cold Outreach Queue', cold_headers, cold_rows),
        ('All USA Prospects', all_headers, all_rows),
    ])

    print({
        'all_count': len(all_rows),
        'reached_count': len(reached_rows),
        'cold_count': len(cold_rows),
        'xlsx': str(xlsx_path),
        'reached_csv': str(reached_csv),
        'cold_csv': str(cold_csv),
        'all_csv': str(all_csv),
    })


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import base64
import csv
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

ROOT = Path('/root/.openclaw/agents/sales-heshbonai/workspace')
SA_KEY = '/root/.heshbonai-sa-key.json'
IMPERSONATE = 'marko@heshbonai.co'
MATTAN = 'mattan@heshbonai.co'
DATE = '2026-03-27'

PLAYBOOK_MD = ROOT / 'handoffs' / 'mattan' / f'HeshbonAI_Mattan_Sales_Playbook_{DATE}.md'
REACHED_CSV = ROOT / 'handoffs' / 'mattan' / f'HeshbonAI_reached_out_USA_{DATE}.csv'
COLD_CSV = ROOT / 'handoffs' / 'mattan' / f'HeshbonAI_cold_outreach_queue_USA_{DATE}.csv'
ALL_CSV = ROOT / 'handoffs' / 'mattan' / f'HeshbonAI_all_USA_prospects_{DATE}.csv'

SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/gmail.send',
]


def get_services():
    creds = service_account.Credentials.from_service_account_file(
        SA_KEY, scopes=SCOPES, subject=IMPERSONATE
    )
    return (
        build('drive', 'v3', credentials=creds),
        build('docs', 'v1', credentials=creds),
        build('sheets', 'v4', credentials=creds),
        build('gmail', 'v1', credentials=creds),
    )


def md_to_doc_text(md_text: str) -> str:
    lines = []
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if line.startswith('# '):
            lines.append(line[2:].upper())
            lines.append('')
            continue
        if line.startswith('## '):
            lines.append(line[3:].upper())
            lines.append('')
            continue
        if line.startswith('### '):
            lines.append(line[4:])
            continue
        if line.startswith('- '):
            lines.append('• ' + line[2:])
            continue
        if re.match(r'^\d+\) ', line):
            lines.append(line)
            continue
        lines.append(line)
    text = '\n'.join(lines)
    text = text.replace('**', '')
    text = text.replace('`', '')
    return text


def read_csv(path: Path):
    with path.open(newline='') as f:
        return list(csv.reader(f))


def ensure_permission(drive, file_id: str, email: str, role: str = 'writer'):
    drive.permissions().create(
        fileId=file_id,
        body={
            'type': 'user',
            'role': role,
            'emailAddress': email,
        },
        sendNotificationEmail=False,
        supportsAllDrives=True,
    ).execute()


def create_folder(drive, name: str):
    meta = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
    }
    folder = drive.files().create(body=meta, fields='id,webViewLink').execute()
    return folder['id'], folder['webViewLink']


def create_doc(drive, docs, folder_id: str, title: str, text: str):
    doc = docs.documents().create(body={'title': title}).execute()
    doc_id = doc['documentId']
    docs.documents().batchUpdate(
        documentId=doc_id,
        body={
            'requests': [
                {
                    'insertText': {
                        'location': {'index': 1},
                        'text': text,
                    }
                }
            ]
        },
    ).execute()
    drive.files().update(fileId=doc_id, addParents=folder_id, removeParents='root', fields='id,webViewLink').execute()
    return doc_id, f'https://docs.google.com/document/d/{doc_id}/edit'


def create_sheet(drive, sheets, folder_id: str, title: str, reached, cold, all_rows):
    ss = sheets.spreadsheets().create(
        body={
            'properties': {'title': title},
            'sheets': [
                {'properties': {'title': 'Reached Out'}},
                {'properties': {'title': 'Cold Outreach Queue'}},
                {'properties': {'title': 'All USA Prospects'}},
            ],
        }
    ).execute()
    ss_id = ss['spreadsheetId']

    # Delete default Sheet1 if present.
    meta = sheets.spreadsheets().get(spreadsheetId=ss_id).execute()
    delete_requests = []
    freeze_requests = []
    for sh in meta.get('sheets', []):
        title_ = sh['properties']['title']
        sid = sh['properties']['sheetId']
        if title_ == 'Sheet1':
            delete_requests.append({'deleteSheet': {'sheetId': sid}})
        else:
            freeze_requests.append({
                'updateSheetProperties': {
                    'properties': {'sheetId': sid, 'gridProperties': {'frozenRowCount': 1}},
                    'fields': 'gridProperties.frozenRowCount'
                }
            })
    if delete_requests or freeze_requests:
        sheets.spreadsheets().batchUpdate(
            spreadsheetId=ss_id,
            body={'requests': delete_requests + freeze_requests}
        ).execute()

    data = [
        {'range': 'Reached Out!A1', 'values': reached},
        {'range': 'Cold Outreach Queue!A1', 'values': cold},
        {'range': 'All USA Prospects!A1', 'values': all_rows},
    ]
    sheets.spreadsheets().values().batchUpdate(
        spreadsheetId=ss_id,
        body={'valueInputOption': 'RAW', 'data': data}
    ).execute()

    drive.files().update(fileId=ss_id, addParents=folder_id, removeParents='root', fields='id,webViewLink').execute()
    return ss_id, f'https://docs.google.com/spreadsheets/d/{ss_id}/edit'


def send_email(gmail, doc_link: str, sheet_link: str, folder_link: str):
    body = f"""Hi Mattan,

I moved everything into Google Drive so it is easier to use and update.

Links:
- Sales playbook (Google Doc): {doc_link}
- USA prospect sheet (Google Sheet): {sheet_link}
- Drive folder: {folder_link}
- HeshbonAI LinkedIn page: https://www.linkedin.com/company/heshbonai/?viewAsMember=true

What is inside the Google Sheet:
- Reached Out
- Cold Outreach Queue
- All USA Prospects

The sales playbook includes:
- cold call opener
- gatekeeper script
- voicemail script
- discovery questions
- 30-second pitch
- objection handling / Q&A
- competitive positioning
- qualification checklist
- follow-up email + text scripts
- pricing / security escalation notes

Best,
Marko
CEO & Founder, HeshbonAI
marko@heshbonai.co | heshbonai.co
"""
    msg = MIMEMultipart()
    msg['To'] = MATTAN
    msg['From'] = f'Marko <{IMPERSONATE}>'
    msg['Subject'] = 'HeshbonAI Google Docs + Sheets handoff for outreach'
    msg.attach(MIMEText(body, 'plain'))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
    result = gmail.users().messages().send(userId='me', body={'raw': raw}).execute()
    return result.get('id')


def main():
    drive, docs, sheets, gmail = get_services()

    folder_id, folder_link = create_folder(drive, f'HeshbonAI - Mattan Handoff - {DATE}')
    ensure_permission(drive, folder_id, MATTAN, 'writer')

    playbook_text = md_to_doc_text(PLAYBOOK_MD.read_text())
    doc_id, doc_link = create_doc(drive, docs, folder_id, 'HeshbonAI - Mattan Sales Playbook', playbook_text)
    ensure_permission(drive, doc_id, MATTAN, 'writer')

    reached = read_csv(REACHED_CSV)
    cold = read_csv(COLD_CSV)
    all_rows = read_csv(ALL_CSV)
    sheet_id, sheet_link = create_sheet(drive, sheets, folder_id, 'HeshbonAI - USA Prospects for Mattan', reached, cold, all_rows)
    ensure_permission(drive, sheet_id, MATTAN, 'writer')

    message_id = send_email(gmail, doc_link, sheet_link, folder_link)

    print({
        'folder_link': folder_link,
        'doc_link': doc_link,
        'sheet_link': sheet_link,
        'gmail_message_id': message_id,
    })


if __name__ == '__main__':
    main()

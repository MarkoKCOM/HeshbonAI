#!/usr/bin/env python3
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2 import service_account
from googleapiclient.discovery import build

SA_KEY = '/root/.heshbonai-sa-key.json'
IMPERSONATE = 'marko@heshbonai.co'
MATTAN = 'mattan@heshbonai.co'
FOLDER_ID = '1S83kd_luDu06Oa4nsljYYJgPbEcNESRQ'
SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/gmail.send',
]


def get_services():
    creds = service_account.Credentials.from_service_account_file(
        SA_KEY, scopes=SCOPES, subject=IMPERSONATE
    )
    return (
        build('drive', 'v3', credentials=creds),
        build('docs', 'v1', credentials=creds),
        build('gmail', 'v1', credentials=creds),
    )


def add_text(requests, index, text, bold=False):
    requests.append({'insertText': {'location': {'index': index}, 'text': text}})
    end = index + len(text)
    if bold:
        requests.append({
            'updateTextStyle': {
                'range': {'startIndex': index, 'endIndex': end},
                'textStyle': {'bold': True},
                'fields': 'bold'
            }
        })
    return end


def add_heading(requests, index, text, level='HEADING_1'):
    start = index
    index = add_text(requests, index, text + '\n')
    requests.append({
        'updateParagraphStyle': {
            'range': {'startIndex': start, 'endIndex': index},
            'paragraphStyle': {'namedStyleType': level},
            'fields': 'namedStyleType'
        }
    })
    return index


def add_paragraph(requests, index, text):
    return add_text(requests, index, text + '\n\n')


def add_bullets(requests, index, items):
    start = index
    text = ''.join(item + '\n' for item in items) + '\n'
    index = add_text(requests, index, text)
    requests.append({
        'createParagraphBullets': {
            'range': {'startIndex': start, 'endIndex': index - 1},
            'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
        }
    })
    return index


def build_doc_requests():
    req = []
    i = 1

    i = add_heading(req, i, 'HeshbonAI - Mattan Sales Playbook', 'TITLE')
    i = add_paragraph(req, i, 'Updated, formatted version for easier reading and live sales use.')

    i = add_heading(req, i, '1. Quick Positioning', 'HEADING_1')
    i = add_paragraph(req, i, 'HeshbonAI is a white-label AI assistant for CPA firms. It automates client communication, follow-up, document collection, question handling, and workflow coordination through WhatsApp and SMS.')
    i = add_bullets(req, i, [
        'White-label - fully branded to the firm',
        'Clients feel like they are talking to a real team member',
        'Works through WhatsApp and SMS',
        'Follows up automatically until documents arrive',
        'Answers routine client questions 24/7',
        'Reads, scans, and analyzes incoming PDFs and files',
        'Keeps status, deadlines, and missing items organized',
        'Integrates with QuickBooks, Google Drive, Dropbox, Google Calendar, Outlook, and Zapier',
    ])

    i = add_heading(req, i, '2. What to Lead With', 'HEADING_1')
    i = add_paragraph(req, i, 'Do not start with AI. Start with the pain.')
    i = add_bullets(req, i, [
        'Your staff is wasting hours chasing clients for documents',
        'Skilled people are doing admin instead of billable work',
        'Deadlines become stressful because files arrive late',
        'Client communication is scattered across email, text, calls, and WhatsApp',
        'Clients ignore portals and email reminders but respond to their phone',
        'Staff keeps answering the same questions again and again',
    ])
    i = add_paragraph(req, i, 'Best line: Most firms do not have a document problem. They have a follow-up problem.')

    i = add_heading(req, i, '3. What to Say / What Not to Say', 'HEADING_1')
    i = add_heading(req, i, 'Say this', 'HEADING_2')
    i = add_bullets(req, i, [
        'AI assistant',
        'Firm-branded',
        'Client communication',
        'Follow-up automation',
        'Routine question handling',
        'Workflow coordination',
    ])
    i = add_heading(req, i, 'Do not say this', 'HEADING_2')
    i = add_bullets(req, i, [
        'Do not call it a bot',
        'Do not say quick setup or 15-minute setup',
        'Do not promise features you are not sure about',
        'Do not give fixed pricing unless approved',
    ])

    i = add_heading(req, i, '4. Cold Call Opener', 'HEADING_1')
    i = add_heading(req, i, 'Direct version', 'HEADING_2')
    i = add_paragraph(req, i, 'Hi, this is Mattan from HeshbonAI. Quick reason for the call - we help CPA firms automate client follow-up, document collection, and routine client communication through a white-label AI assistant on WhatsApp and SMS. A lot of firms we speak with are still spending way too much staff time chasing clients for documents. Is that something your team still deals with manually?')
    i = add_heading(req, i, 'Softer version', 'HEADING_2')
    i = add_paragraph(req, i, 'Hi, this is Mattan from HeshbonAI. We work with CPA firms that are tired of chasing clients for documents and routine replies. We help automate that with a firm-branded AI assistant over WhatsApp and SMS. Just curious - how is your team handling document follow-up today?')

    i = add_heading(req, i, '5. Gatekeeper Script', 'HEADING_1')
    i = add_paragraph(req, i, 'Hi, maybe you can point me in the right direction. I am trying to reach the person who handles operations, client communication, or workflow decisions for the firm. We help CPA firms automate client follow-up and document collection through a white-label AI assistant on WhatsApp and SMS. Who would be the best person to speak with about that?')
    i = add_paragraph(req, i, 'If they ask you to email first: Absolutely. What is the best email for them, and what is their name so I can send a short note?')

    i = add_heading(req, i, '6. Discovery Questions', 'HEADING_1')
    i = add_bullets(req, i, [
        'How are you currently collecting documents from clients?',
        'Is that mostly email, phone, portal, text, or WhatsApp today?',
        'How much staff time goes into reminders and follow-up each week?',
        'Who on the team usually owns that process?',
        'What usually causes the biggest delays - no response, incomplete files, wrong files, or late submissions?',
        'Are clients asking the same routine questions over and over?',
        'Do you already use a portal or practice management platform?',
        'Do your clients respond better to text / WhatsApp than email?',
        'Is this more of a tax-season pain or year-round pain?',
    ])

    i = add_heading(req, i, '7. 30-Second Pitch', 'HEADING_1')
    i = add_paragraph(req, i, 'Based on what you said, HeshbonAI sounds relevant because it takes the repetitive client-facing work off your team. It works as a white-label AI assistant under your firm\'s name, messages clients through WhatsApp and SMS, follows up automatically until documents arrive, answers routine questions, reads incoming files, and keeps the whole process organized. So instead of your team manually chasing every client, they only step in when real attention is needed.')

    i = add_heading(req, i, '8. Book the Demo', 'HEADING_1')
    i = add_bullets(req, i, [
        'Would it make sense to show you how it works on a quick call?',
        'The easiest next step is a short walkthrough so you can see whether it fits your workflow.',
        'What does your calendar look like this week or next?',
    ])

    i = add_heading(req, i, '9. Objections and Answers', 'HEADING_1')
    objections = [
        ('We already use email or a portal', 'Most firms we speak with already have some process in place. The issue is usually not whether a process exists - it is whether clients actually respond fast enough and whether your staff still has to keep chasing. HeshbonAI helps when the current process still depends on manual follow-up and scattered replies.'),
        ('Our clients are older. They do not use WhatsApp', 'That is exactly why SMS matters too. For firms with clients who prefer text, HeshbonAI can support communication there as well. The bigger point is meeting clients where they already respond instead of forcing them into a portal habit.'),
        ('We already text clients manually', 'Right - and that usually works better than email. What HeshbonAI changes is that your team does not have to keep doing it manually. It automates the reminders, tracks what is still missing, answers routine questions, and keeps the workflow organized.'),
        ('How is this different from TaxDome, Liscio, or Canopy?', 'Those platforms are broader practice management or portal tools. HeshbonAI is focused on the client-facing workflow that usually still stays manual - follow-up, document chasing, routine client communication, and keeping that flow moving through WhatsApp and SMS.'),
        ('We do not want AI talking to clients', 'Totally fair. HeshbonAI is designed as a firm-branded AI assistant under your firm\'s identity. The point is not to sound robotic. The point is to handle routine communication clearly, professionally, and consistently while your team stays in control.'),
        ('Does it only do document collection?', 'No. That is usually the entry point, but it is broader than that. It automates client communication, reminders, question handling, workflow coordination, and status tracking - not just document requests.'),
        ('Does it integrate with our tools?', 'Yes - the integrations we talk about today are QuickBooks, Google Drive, Dropbox, Google Calendar, Outlook, and Zapier.'),
        ('How much does it cost?', 'Pricing depends on the firm\'s size, workflow, and use case. The best thing is to scope that after a short conversation once we understand volume and needs.'),
    ]
    for q, a in objections:
        i = add_heading(req, i, q, 'HEADING_2')
        i = add_paragraph(req, i, a)

    i = add_heading(req, i, '10. Qualification Checklist', 'HEADING_1')
    i = add_bullets(req, i, [
        '2+ staff members',
        'Recurring tax, bookkeeping, or document-heavy workflows',
        'Clients who respond slowly by email',
        'Team currently spending time on reminders and status checks',
        'Growing firm or multi-location firm',
        'Client base comfortable with text or WhatsApp',
        'Frustration around late or incomplete submissions',
    ])

    i = add_heading(req, i, '11. Escalate These Questions', 'HEADING_1')
    i = add_bullets(req, i, [
        'Formal quote requests',
        'Contract terms',
        'Discounting',
        'Annual pricing commitments',
        'Security review paperwork',
        'Legal compliance questions',
        'Data retention policy',
        'Enterprise procurement',
    ])

    i = add_heading(req, i, '12. Follow-Up Templates', 'HEADING_1')
    i = add_heading(req, i, 'Email follow-up', 'HEADING_2')
    i = add_paragraph(req, i, 'Hi [Name],\n\nGood speaking with you today.\n\nAs discussed, HeshbonAI helps CPA firms automate client communication, follow-up, document collection, routine questions, and workflow coordination through a white-label AI assistant on WhatsApp and SMS.\n\nThe main value is simple - less staff time spent chasing, better client response rates, and a more organized workflow.\n\nHappy to show you how it works in a short walkthrough.\n\nBest,\nMattan')
    i = add_heading(req, i, 'Text follow-up', 'HEADING_2')
    i = add_paragraph(req, i, 'Hi [Name] - Mattan here from HeshbonAI. Good speaking with you earlier. We help CPA firms automate client follow-up, document collection, and routine client communication through a white-label AI assistant on WhatsApp and SMS. Happy to show you how it works when you have 15 minutes.')

    i = add_heading(req, i, '13. Final Reminder', 'HEADING_1')
    i = add_bullets(req, i, [
        'Do not oversell',
        'Be clear',
        'Be direct',
        'Lead with pain',
        'Keep the ask simple',
        'The first call is about getting the next step, not explaining everything',
    ])
    i = add_paragraph(req, i, 'Best closing line: If this is still a manual pain for your team, it probably makes sense for you to see it.')

    return req


def share_file(drive, file_id):
    drive.permissions().create(
        fileId=file_id,
        body={'type': 'user', 'role': 'writer', 'emailAddress': MATTAN},
        sendNotificationEmail=False,
        supportsAllDrives=True,
    ).execute()


def send_update_email(gmail, doc_link):
    body = f'''Hi Mattan,

I updated the HeshbonAI sales playbook into a cleaner Google Doc structure so it is easier to read and use during calls.

Updated playbook:
{doc_link}

This version is organized with:
- clear sections
- headings and subheadings
- skimmable bullets
- cleaner objection handling
- easier call flow

Best,
Marko
CEO & Founder, HeshbonAI
marko@heshbonai.co | heshbonai.co
'''
    msg = MIMEMultipart()
    msg['To'] = MATTAN
    msg['From'] = f'Marko <{IMPERSONATE}>'
    msg['Subject'] = 'Updated HeshbonAI sales playbook - formatted Google Doc'
    msg.attach(MIMEText(body, 'plain'))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
    result = gmail.users().messages().send(userId='me', body={'raw': raw}).execute()
    return result.get('id')


def main():
    drive, docs, gmail = get_services()
    doc = docs.documents().create(body={'title': 'HeshbonAI - Mattan Sales Playbook (Formatted)'}).execute()
    doc_id = doc['documentId']
    docs.documents().batchUpdate(documentId=doc_id, body={'requests': build_doc_requests()}).execute()
    drive.files().update(fileId=doc_id, addParents=FOLDER_ID, removeParents='root', fields='id,webViewLink').execute()
    share_file(drive, doc_id)
    link = f'https://docs.google.com/document/d/{doc_id}/edit'
    gmail_id = send_update_email(gmail, link)
    print({'doc_link': link, 'gmail_message_id': gmail_id})


if __name__ == '__main__':
    main()

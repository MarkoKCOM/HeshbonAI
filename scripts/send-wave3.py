#!/usr/bin/env python3
"""
Wave 3 - Send 20 cold emails (#40-59) using v5.2 templates.
Uses Gmail API via service account with domain-wide delegation.
Sender: marko@heshbonai.co
"""

import base64
import time
import json
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2 import service_account
from googleapiclient.discovery import build

SA_KEY = "/root/.heshbonai-sa-key.json"
SENDER = "marko@heshbonai.co"
SENDER_NAME = "Marko"
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

SIGNATURE = """Best,
Marko
CEO & Founder, HeshbonAI
marko@heshbonai.co | heshbonai.co

---
To opt out, reply "unsubscribe" and I'll remove you immediately.
HeshbonAI - 30 N Gould St, Ste R, Sheridan, WY 82801"""

# --- TEMPLATES v5.2 ---

def template_A(first_name, firm_name):
    """Sequence A: The Document Problem"""
    subject_options = [
        f"{firm_name} - still chasing clients for documents?",
        f"The follow-ups killing your team's time at {firm_name}",
        f"Quick question about document collection at {firm_name}",
    ]
    body = f"""Hi {first_name},

Your team is spending hours every week sending reminders, checking who replied, and following up again. That's skilled staff doing admin instead of billable work.

HeshbonAI handles it - a white-label AI assistant that works under your firm's name. Clients think it's a real team member, not software.

- Messages clients on WhatsApp and text - 90%+ response rate
- Follows up automatically until documents arrive
- Reads, scans, and analyzes incoming PDFs and files
- Answers client questions 24/7
- Syncs with QuickBooks, Google Drive, Dropbox, Google Calendar, Outlook, and Zapier

Worth a 15-minute call to see if it fits {firm_name}?

{SIGNATURE}"""
    return subject_options, body


def template_B(first_name, firm_name, tech_signal):
    """Sequence B: The Tech-Forward Firm"""
    subject_options = [
        f"{firm_name}'s next automation win",
        f"The one workflow {firm_name} probably hasn't automated yet",
    ]
    body = f"""Hi {first_name},

{firm_name} is already doing things the modern way - {tech_signal}. But there's one workflow almost every firm still does manually - chasing clients for documents.

HeshbonAI is a white-label AI assistant that works under your firm's name. Clients think they're talking to a real person on your team.

- Messages clients on WhatsApp and text - 90%+ response rate
- Follows up automatically until documents arrive
- Reads and analyzes incoming PDFs and files
- Answers client questions 24/7
- Plugs into QuickBooks, Google Drive, Dropbox, Google Calendar, Outlook, and Zapier

Worth a 15-minute call to see how it fits your setup?

{SIGNATURE}"""
    return subject_options, body


def template_C(first_name, firm_name, diversity_signal, languages):
    """Sequence C: The Diverse Client Base"""
    subject_options = [
        f"{firm_name} - reaching clients who prefer WhatsApp",
        f"Document collection for {firm_name}'s diverse client base",
    ]
    body = f"""Hi {first_name},

{firm_name} serves {diversity_signal} - a client base where WhatsApp isn't just convenient, it's how they communicate. Collecting documents via email or portals doesn't work here. Low response rates, language barriers, apps they'll never download.

HeshbonAI is built for exactly this - a white-label AI assistant that messages clients in {languages} via WhatsApp under your firm's name. Clients think they're talking to a real team member.

- Follows up automatically until documents arrive
- Reads and analyzes incoming documents
- Answers client questions 24/7 in their language
- Tracks everything in one dashboard - 90%+ response rate
- Syncs with QuickBooks, Google Drive, Dropbox, Google Calendar, Outlook, and Zapier

Worth a quick conversation?

{SIGNATURE}"""
    return subject_options, body


# --- PROSPECT DATA ---
# Each: (prospect_num, firm_name, first_name, email, sequence, tech_signal/diversity_signal, subject_variant_index)

PROSPECTS = [
    # Wave 3: #40-49
    (40, "Sai CPA Services", "Ajay", "info@saicpaservices.com", "B",
     "QuickBooks, virtual CFO model, cloud services", 0),
    (41, "Demian & Company, LLC", "Peter", "info@taxprocpa.com", "A",
     None, 0),
    (42, "Brooks & Associates, CPAs, Inc.", "there", "info@brookscpafirm.com", "B",
     "QuickBooks certified, small business focus", 1),
    (43, "Blankenship CPA Group, PLLC", "there", "info@bcpas.com", "A",
     None, 1),
    (44, "Lewis CPA LLC", "Marye", "marye@lewiscpallc.com", "B",
     "QuickBooks, SecureSend, client portal", 0),
    (45, "Silicon Valley CPA Firm", "there", "jph@siliconvalleyCPAFirm.com", "B",
     "QuickBooks, multiple industry verticals, Silicon Valley tech roots", 1),
    (46, "K. A. Lindow, CPA, P.C.", "Ken", "ken@lindowcpa.com", "B",
     "QuickBooks, outsourced CPA model, nationwide service", 0),
    (47, "Bryant & Associates, LLC", "Travareis", "travareis@bryantcpallc.com", "B",
     "QuickBooks, cryptocurrency services, client portal", 1),
    (48, "Matthew P. Schlanger CPA LLC", "Matthew", "matthew@cpaschlanger.com", "B",
     "QuickBooks, CFO services, modern website", 0),
    (49, "Jaffer Merchant, CPA", "Jaffer", "info@jaffermerchantcpa.com", "B",
     "QuickBooks, client portal, modern practice", 1),

    # Wave 4 first 10: #50-59
    (50, "CPA 1099", "there", "info@cpa1099.com", "A",
     None, 2),
    (51, "Harlem CPA", "there", "info@cpaharlem.com", "C",
     "a diverse client base in Harlem", "English and Spanish", 0),
    (52, "Friedman & Associates PA", "Marc", "marc@friedmancpa.com", "A",
     None, 0),
    (53, "RALL CPA", "there", "druocco@rallcpa.com", "A",
     None, 1),
    (54, "NCL CPA Firm", "there", "contact@ncllcpa.com", "A",
     None, 2),
    (55, "Raymond Lyle CPA PLLC", "Andrew", "andrew@raymondlylecpa.com", "B",
     "modern accounting services in Seattle's tech hub", 0),
    (56, "Seattle Tax Group LLC", "Brian", "brian@seattletaxgroup.com", "B",
     "CPA and accounting services in Seattle's tech-forward market", 1),
    (57, "Lockhart & Powell CPAs", "there", "reception@lockhartandpowell.com", "A",
     None, 0),
    (58, "Pillai CPA", "there", "taxinfo@pillaicpa.com", "C",
     "a diverse client base in the Dallas area", "English and Hindi", 1),
    (59, "Hollis CPA Firm", "Cameron", "cameron@holliscpa.com", "A",
     None, 1),
]

def get_gmail_service():
    creds = service_account.Credentials.from_service_account_file(
        SA_KEY, scopes=SCOPES, subject=SENDER
    )
    return build("gmail", "v1", credentials=creds)

def create_message(to, subject, body_text):
    msg = MIMEMultipart("alternative")
    msg["To"] = to
    msg["From"] = f"{SENDER_NAME} <{SENDER}>"
    msg["Subject"] = subject
    
    # Plain text
    msg.attach(MIMEText(body_text, "plain"))
    
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    return {"raw": raw}

def send_email(service, to, subject, body):
    message = create_message(to, subject, body)
    result = service.users().messages().send(userId="me", body=message).execute()
    return result.get("id", "unknown")

def main():
    service = get_gmail_service()
    results = []
    
    for i, prospect in enumerate(PROSPECTS):
        # Handle Sequence C with extra field (diversity_signal is in index 5, languages in index 6)
        if prospect[4] == "C":
            num, firm, first, email, seq, div_signal, languages, subj_idx = (
                prospect[0], prospect[1], prospect[2], prospect[3], prospect[4],
                prospect[5], prospect[6], prospect[7] if len(prospect) > 7 else 0
            )
            subject_options, body = template_C(first, firm, div_signal, languages)
            subject = subject_options[subj_idx % len(subject_options)]
        elif prospect[4] == "B":
            num, firm, first, email, seq, tech_signal, subj_idx = prospect
            subject_options, body = template_B(first, firm, tech_signal)
            subject = subject_options[subj_idx % len(subject_options)]
        else:  # A
            num, firm, first, email, seq, _, subj_idx = prospect
            subject_options, body = template_A(first, firm)
            subject = subject_options[subj_idx % len(subject_options)]
        
        try:
            msg_id = send_email(service, email, subject, body)
            status = "SENT"
            print(f"[{i+1}/20] ✅ #{num} {firm} -> {email} | Subject: {subject} | Gmail ID: {msg_id}")
        except Exception as e:
            status = f"FAILED: {e}"
            print(f"[{i+1}/20] ❌ #{num} {firm} -> {email} | {status}")
        
        results.append({
            "num": num,
            "firm": firm,
            "email": email,
            "sequence": seq,
            "subject": subject,
            "status": status
        })
        
        # Stagger sends - 8-12 second delay between emails
        if i < len(PROSPECTS) - 1:
            delay = 8 + (i % 5)  # 8-12 seconds
            time.sleep(delay)
    
    # Summary
    sent = sum(1 for r in results if r["status"] == "SENT")
    failed = sum(1 for r in results if r["status"] != "SENT")
    print(f"\n{'='*60}")
    print(f"DONE: {sent} sent, {failed} failed out of {len(results)}")
    
    if failed > 0:
        print("\nFailed emails:")
        for r in results:
            if r["status"] != "SENT":
                print(f"  #{r['num']} {r['firm']} - {r['status']}")
    
    # Write results to JSON for logging
    with open("/root/.openclaw/agents/sales-heshbonai/workspace/scripts/wave3-results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to scripts/wave3-results.json")

if __name__ == "__main__":
    main()

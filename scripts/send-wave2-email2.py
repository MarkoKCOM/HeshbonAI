#!/usr/bin/env python3
"""
Wave 2 Email 2 Follow-Ups - 20 firms (#11-30)
Originally contacted March 12. Email 2 was due March 16 (3 days overdue).
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


def email2_A(first_name):
    """Sequence A Email 2: Document Problem follow-up"""
    return f"""Hi {first_name},

Following up - one thing worth knowing.

When clients send documents, HeshbonAI reads, scans, and analyzes every file automatically - catches errors and missing items before your team even opens them. Wrong document? Incomplete? It flags it and asks the client to resubmit.

And it answers client questions around the clock - "did you get my documents?", "what's still missing?", "when's the deadline?" - so your staff stops fielding those calls.

Want me to walk you through how it works on a quick call?

{SIGNATURE}"""


def email2_B(first_name, firm_name):
    """Sequence B Email 2: Tech-Forward follow-up"""
    return f"""Hi {first_name},

Quick follow-up - the number that surprises most firms: 90%+ client response rate.

That's what happens when you message clients where they actually respond instead of email portals. HeshbonAI puts it all on autopilot - fully branded to {firm_name}, with AI that reads and classifies every document that comes in.

Worth a quick call to see how it works?

{SIGNATURE}"""


def email2_C(first_name):
    """Sequence C Email 2: Diverse Client Base follow-up (same structure as A with WhatsApp angle)"""
    return f"""Hi {first_name},

Following up - one thing worth knowing.

When clients send documents through WhatsApp, HeshbonAI reads, scans, and analyzes every file automatically - catches errors and missing items before your team even opens them. Wrong document? Incomplete? It messages the client back in their language and asks them to resubmit.

And it answers client questions around the clock - "did you get my documents?", "what's still missing?", "when's the deadline?" - in the language they're most comfortable with.

Want me to walk you through how it works on a quick call?

{SIGNATURE}"""


# Wave 2 prospects: (num, firm_name, first_name, email, sequence, original_subject)
PROSPECTS = [
    (11, "Mei CPA PC", "there", "info@meicpa.com", "C",
     "Mei CPA PC - reaching clients who prefer WhatsApp"),
    (12, "MiamiCPA LLC", "Glenn", "glenn@miamicpa.com", "C",
     "Document collection for MiamiCPA LLC's diverse client base"),
    (13, "Debbie Griffiths CPA LLC", "Debbie", "info@griffithsatlanta.com", "B",
     "Debbie Griffiths CPA LLC's next automation win"),
    (14, "The Atlanta CPA Group LLC", "there", "info@atlcpagroup.com", "B",
     "The one workflow The Atlanta CPA Group LLC probably hasn't automated yet"),
    (15, "SMB CPA Group, PC", "there", "contact@smbcpagroup.com", "B",
     "SMB CPA Group, PC's next automation win"),
    (16, "B.O.L. Global, Inc.", "there", "info@bolglobalcpa.com", "B",
     "The one workflow B.O.L. Global, Inc. probably hasn't automated yet"),
    (17, "San Diego CPA", "there", "info@sandiegocpas.com", "B",
     "San Diego CPA's next automation win"),
    (18, "Thomas Huckabee, CPA, Inc.", "Thomas", "thomas.huckabee@tehcpa.net", "B",
     "The one workflow Thomas Huckabee, CPA, Inc. probably hasn't automated yet"),
    (19, "Perpetual CPA", "there", "info@perpetualcpa.com", "B",
     "Perpetual CPA's next automation win"),
    (20, "O'Connor CPA Firm, LLC", "Tricia", "Tricia@OConnorCPAFirm.com", "B",
     "The one workflow O'Connor CPA Firm, LLC probably hasn't automated yet"),
    (21, "MacAlpine Carll and Co., LLC", "there", "cpa@macalpinecarll.com", "A",
     "MacAlpine Carll and Co., LLC - still chasing clients for documents?"),
    (22, "GLSC & Company PLLC", "there", "info@glsccpa.com", "A",
     "The follow-ups killing your team's time at GLSC & Company PLLC"),
    (23, "Parsons CPA, PLLC", "there", "accounting@parsonscpa.com", "A",
     "Quick question about document collection at Parsons CPA, PLLC"),
    (24, "Carolina Accounting & Tax Service", "there", "service@carolinaaccounting.com", "A",
     "Carolina Accounting & Tax Service - still chasing clients for documents?"),
    (25, "Stenger Tax Advisory", "Chris", "Chris.Jordan@stengerfamilyoffice.com", "A",
     "The follow-ups killing your team's time at Stenger Tax Advisory"),
    (26, "Rapacki + Co", "Joe", "joe@rapacki.com", "A",
     "Quick question about document collection at Rapacki + Co"),
    (27, "L&H CPAs and Advisors", "there", "info@lhcpafirm.com", "A",
     "L&H CPAs and Advisors - still chasing clients for documents?"),
    (28, "MJ Ahmed CPA PLLC", "MJ", "mj@dallascpa.net", "A",
     "The follow-ups killing your team's time at MJ Ahmed CPA PLLC"),
    (29, "Jarrar & Associates CPA, Inc.", "Sam", "samcpa@jarrarcpa.com", "A",
     "Quick question about document collection at Jarrar & Associates CPA, Inc."),
    (30, "Neumann Curtis CPAs", "there", "info@neumanncurtis.com", "A",
     "Neumann Curtis CPAs - still chasing clients for documents?"),
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

    for i, (num, firm, first, email, seq, orig_subj) in enumerate(PROSPECTS):
        subject = f"Re: {orig_subj}"

        if seq == "A":
            body = email2_A(first)
        elif seq == "B":
            body = email2_B(first, firm)
        elif seq == "C":
            body = email2_C(first)
        else:
            body = email2_A(first)

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

        # Stagger sends - 8-12 second delay
        if i < len(PROSPECTS) - 1:
            delay = 8 + (i % 5)
            time.sleep(delay)

    sent = sum(1 for r in results if r["status"] == "SENT")
    failed = sum(1 for r in results if r["status"] != "SENT")
    print(f"\n{'='*60}")
    print(f"DONE: {sent} sent, {failed} failed out of {len(results)}")

    if failed > 0:
        print("\nFailed emails:")
        for r in results:
            if r["status"] != "SENT":
                print(f"  #{r['num']} {r['firm']} - {r['status']}")

    with open("/root/.openclaw/agents/sales-heshbonai/workspace/scripts/wave2-email2-results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to scripts/wave2-email2-results.json")


if __name__ == "__main__":
    main()

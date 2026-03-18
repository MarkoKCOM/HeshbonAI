# TOOLS.md — Local Environment

## Google Workspace Access (USE THIS — you have full API access)

You have a **service account with domain-wide delegation** on heshbonai.co. This means you can:
- **Send emails** as marko@heshbonai.co via Gmail API
- **Read/write Google Sheets** (pipeline tracker, prospect data)
- **Read/write Google Docs** (proposals, one-pagers)
- **Access Google Drive** (shared files, attachments)
- **Manage Google Contacts**

**How to use it:**
- **Service Account:** `marko-agent@heshbonai-489415.iam.gserviceaccount.com`
- **SA Key file:** `/root/.heshbonai-sa-key.json` (chmod 600)
- **Impersonate:** `marko@heshbonai.co` (domain-wide delegation)
- **Scopes:** Gmail send/read, Sheets, Docs, Drive, Contacts
- **Example script:** `scripts/send-wave3.py` — uses the SA key to send emails via Gmail API

**To send emails:** Write a Python script using `google.oauth2.service_account` + `googleapiclient`. See `scripts/send-wave3.py` as the working reference. You built this — use it.

**To read/write Sheets:** Same auth pattern, use `sheets` service instead of `gmail`.

## Links & Resources
- **Website:** https://heshbonai.co
- **Pipeline Sheet:** https://docs.google.com/spreadsheets/d/1U4fxAA-IrxBgJ0ztAdLn9U1AqfOvWPdRGiXsU3rhmU8
- **GitHub Repo:** https://github.com/MarkoKCOM/HeshbonAI

## Local File Paths (all inside this workspace)

### Prospects (all in `prospects/`)
- USA prospects (162 firms): `prospects/targets-usa.md`
- Israel prospects (87 firms): `prospects/targets-israel.md`
- Master dedup tracker: `prospects/master-tracker.md`
- Sales pipeline: `prospects/pipeline.md`
- Wave 3 research: `prospects/wave3-research.md`

### Business
- Brand guide: `business/branding/brand-guide.md`
- Product positioning: `business/product/positioning.md`
- Product features: `business/product/features.md`
- One-pager: `business/product/one-pager.md`
- Competitor analysis: `business/competitors/analysis.md`
- Website copy: `business/website/`

### Outreach
- Email templates: `templates/email-sequences.md`
- Writing conventions: `memory/writing-conventions.md`
- Outreach log: `memory/outreach-log.md`
- Send script: `scripts/send-wave3.py`

## Domain Warm-Up Rules
- Week 1-2: Max 5 emails/day
- Week 3-4: Max 10 emails/day
- Week 5+: Max 20 emails/day
- Always stagger sends (not all at once)
- Monitor bounce rate — stop if >5%

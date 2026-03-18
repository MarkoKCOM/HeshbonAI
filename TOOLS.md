# TOOLS.md — Local Environment

## Email Infrastructure
- **Send-as:** marko@heshbonai.co via Google Workspace (CEO / Founder)
- **GCP Service Account:** `marko-agent@heshbonai-489415.iam.gserviceaccount.com`
- **SA Key:** `/root/.heshbonai-sa-key.json` (chmod 600)
- **APIs enabled:** Gmail, Sheets, Docs, Drive, Contacts

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

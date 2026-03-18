# HeshbonAI - AI Assistant for CPA Firms

**Brand Name:** HeshbonAI
**Market:** Israeli CPAs/Accountants (Hebrew-first, English supported)
**Strategy:** Sell before building -- validate with real prospects first
**Repo:** Marko's workspace (not KASPACOM)

## Architecture: HeshbonAI vs John

- **HeshbonAI** = the company/business entity. Website at heshbonai.co, Google Workspace, Marko agent handles business operations (sales, marketing, ops).
- **John** = the AI assistant product for CPA firms. When customers sign up, John gets deployed as a firm-branded assistant (e.g., "Maya from Cohen & Co."). John is the product we sell. Each CPA firm gets their own John instance.

The GCP service account (`marko-agent@heshbonai-489415.iam.gserviceaccount.com`) is for HeshbonAI business operations only -- NOT for John product instances.

## Directory Structure

```
heshbonai/
├── README.md              # This file
├── competitors/           # Competitor analysis and website teardowns
├── prospects/             # Target accountant list (50+)
├── website/               # Website copy, structure, design specs
├── product/               # Product specs, feature list, pricing
└── branding/              # Brand guide, messaging, positioning
```

## Status

- [x] Business plan (../cpa-business-plan.md)
- [x] Executive summary (../cpa-business-summary.md)
- [x] Competitor analysis + website teardowns (competitors/analysis.md)
- [x] 50 Israeli accountant prospect list (prospects/targets.md)
- [x] Website structure and copy (website/)
- [x] Product positioning (product/positioning.md)
- [x] Sales one-pager (product/one-pager.md)
- [x] Feature specs MVP vs Future (product/features.md)
- [x] Brand guide + messaging (branding/brand-guide.md)
- [x] Domain purchase -- heshbonai.co (GoDaddy)
- [x] Website built and deployed -- Astro + Tailwind on Vercel (github.com/MarkoKCOM/john-cpa-website)
- [x] DNS configured -- A record + CNAME pointing to Vercel
- [x] www.heshbonai.co live and serving
- [x] Google Workspace -- marko@heshbonai.co (CEO: Marko Sione)
- [x] Email aliases -- john@heshbonai.co, support@heshbonai.co
- [x] Marko health check -- /root/marko-health-check.sh, cron every 5 min, alerts to Sione DM
- [x] HeshbonAI rebrand -- updated brand guide, positioning, homepage copy, site structure (2026-03-07)
- [x] GCP project (heshbonai-489415) + service account key (/root/.heshbonai-sa-key.json)
- [x] Domain-wide delegation in Google Workspace admin (all scopes)
- [x] APIs enabled: Gmail, Calendar, Sheets, Docs, Drive, Admin SDK, Contacts
- [x] Marko agent configured with Google Workspace access (TOOLS.md + .env)
- [ ] Add root domain heshbonai.co (no www) in Vercel domains -- SSL cert missing on root
- [ ] Add MX records in GoDaddy for Google Workspace email routing
- [ ] Formspree integration on contact page form
- [ ] Sales outreach to Tier 2 prospects

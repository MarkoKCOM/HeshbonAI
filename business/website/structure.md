# HeshbonAI Website Structure

## Site Map

### Primary Pages

| Page | URL | Purpose |
|------|-----|---------|
| Homepage | `/` | Convert visitors to demo bookings. Hero + trust + problem + how it works + product UI + pricing + FAQ + CTA |
| Pricing | `/pricing` | Tier comparison (Starter / Professional / Complete) + FAQ |
| How It Works | `/how-it-works` | 3-step walkthrough with WhatsApp conversation and dashboard screenshots |
| About | `/about` | Team, mission, trust signals. Israeli market focus |
| Book Demo | `/demo` | Book a live demo. Calendly embed |
| Login | `/login` | CPA dashboard access (post-launch) |
| Legal | `/privacy`, `/terms` | Privacy policy, terms of service |

### Secondary Pages (Phase 2)

| Page | URL | Purpose |
|------|-----|---------|
| Blog | `/blog` | SEO content: tax season tips, document management, automation |
| Case Studies | `/case-studies` | Named CPA firms with measurable results |
| Integrations | `/integrations` | Accounting software compatibility (Hashavshevet, Priority, etc.) |
| Security | `/security` | Data handling, encryption, WhatsApp Business API compliance |

---

## Navigation

**Logo:** HeshbonAI (left)

**Links:** Product | How It Works | Pricing | FAQ

**CTA Button:** Book a Demo (right, Electric Blue `#2D7FF9` background)

**Language toggle:** EN / HE (Phase 2)

---

## Homepage Sections (scroll order)

1. **Navigation Bar**
   - Logo (HeshbonAI)
   - Links: Product | How It Works | Pricing | FAQ
   - CTA button: "Book a Demo"
   - Language toggle: EN / HE (Phase 2)

2. **Hero Section**
   - Headline: "The AI Assistant for CPA Firms"
   - Subheadline: "Automate client follow-up, document collection, and status tracking through WhatsApp."
   - Primary CTA: "Book a Demo"
   - Secondary CTA: "See How It Works"

3. **Trust Section** (immediately after hero)
   - Clean badge row: WhatsApp Business API | End-to-End Encrypted | SOC 2 | Hebrew-First
   - Minimal design, builds credibility before any selling

4. **Problem Section**
   - "The document chase is costing you hours every week."
   - 3 problem cards: manual follow-up, no visibility, deadline risk

5. **How It Works**
   - Step 1: Assign documents
   - Step 2: HeshbonAI follows up on WhatsApp
   - Step 3: Your team tracks progress in the dashboard

6. **Product UI Showcase** (high on page, before testimonials)
   - Full-width dashboard mockup or interactive screenshot
   - Shows real product UI: client list, document status, deadline tracking
   - Dark navy aesthetic matching brand

7. **WhatsApp + System View**
   - Split view: WhatsApp conversation (left) + dashboard status (right)
   - Shows the same client in both views
   - Annotated callouts: firm-branded, context-aware, persistent, WhatsApp-native

8. **Benefits / Outcomes**
   - 4 outcome cards: hours saved, collection rate, deadline confidence, full visibility

9. **Security & Control**
   - Encryption, API compliance, data isolation, audit trail, human override, SOC 2

10. **Pricing**
    - 3 tiers: Starter (1,000 NIS) | Professional (1,800 NIS) | Complete (2,700 NIS)
    - "14-day free trial. No credit card."

11. **FAQ**
    - 8 questions covering: how it works, Hebrew support, security, setup time, control

12. **Final CTA Section**
    - "Stop Chasing. Start Closing."
    - Book a Demo button + email contact

13. **Footer**
    - Links: Privacy | Terms | Contact | About
    - Social: LinkedIn
    - "Made in Israel" badge
    - Copyright

---

## Design Direction

- **Aesthetic**: Dark navy primary (`#0A1628` / `#111C30`). Clean, premium, minimal. Inspired by Stripe, Linear, Notion.
- **Product UI mockups**: Featured prominently high on the page. Show the actual dashboard, not generic illustrations.
- **Trust section**: Immediately after hero, before any selling content.
- **Typography**: Inter (Latin) + Heebo (Hebrew). JetBrains Mono for data/numbers.
- **Colors**: Deep Navy backgrounds, Electric Blue (`#2D7FF9`) CTAs, Soft Blue (`#6EA8FE`) hover states, Off White (`#E8ECF1`) text, Cool Gray (`#8A95A8`) secondary text, Border Gray (`#263247`) dividers.
- **Illustrations**: WhatsApp conversation mockups + real dashboard screenshots. No generic stock photos.
- **Mobile-first**: 60%+ traffic expected from mobile (Israeli market behavior).
- **Speed**: Target < 2s LCP. Static site (Astro + Tailwind on Vercel).
- **Analytics**: Mixpanel or PostHog for funnel tracking. Google Analytics as backup.
- **Forms**: Calendly embed for demo booking.

---

## Conversion Funnel

```
Visit Homepage
    |
    v
See product UI + problem framing (engagement)
    |
    v
Click "Book a Demo"
    |
    v
Calendly booking page (name, email, firm name, client count)
    |
    v
Demo call completed
    |
    v
Trial activation
```

---

## SEO Target Keywords

- AI assistant for CPA firms
- WhatsApp automation for accountants
- Automated client document collection
- Tax document collection software Israel
- AI accounting assistant Israel
- CPA document management automation
- HeshbonAI

# Email Templates — USA CPA Outreach

**Sender:** Marko <marko@heshbonai.co>
**Sender title:** CEO & Founder, HeshbonAI
**Signature block:** See bottom of this file.

All templates use `{{variables}}` — personalize before sending.

---

## Sequence A: "The Document Problem" (Primary)

Best for: Firms with 30+ clients, tax prep focus, document-heavy industries.

### Email 1 — Cold Open (Day 0)

**Subject options (A/B test):**
- A: `{{firmName}} — still chasing clients for documents?`
- B: `How {{firmName}} could save 10+ hours/week on document collection`
- C: `Quick question about document collection at {{firmName}}`

**Body:**

```
Hi {{firstName}},

I noticed {{firmName}} serves {{specialization}} clients in {{city}} — that usually means a lot of documents to collect every tax season.

Quick question: how much time does your team spend following up with clients for missing documents? For most firms your size, it's 10-15 hours per week.

We built HeshbonAI to eliminate that. It's an AI assistant that reaches out to your clients via text/WhatsApp, follows up automatically on a schedule you set, and tracks everything in a real-time dashboard. Your clients respond because it messages them where they already are — not in a portal they'll never log into.

Firms using it cut document collection time by over 70%.

Would you be open to a 15-minute demo? I can show you exactly how it would work for {{firmName}}.

{{signature}}
```

### Email 2 — Follow-Up Value Add (Day 4)

**Subject:** `Re: {{originalSubject}}`

**Body:**

```
Hi {{firstName}},

Following up on my note from last week. I know tax season keeps everyone buried.

One thing I didn't mention — HeshbonAI sends messages branded to your firm. Your clients see "{{exampleAssistantName}} from {{firmName}}", not a generic tool. It feels like a real team member handling the follow-ups.

Here's what that looks like in practice:
- Client gets a text: "Hi Sarah, this is Maya from {{firmName}}. We need your W-2 and bank statements for your 2025 return. You can reply right here with photos or PDFs."
- Client snaps a photo, sends it back.
- Dashboard updates automatically. No spreadsheet. No phone tag.

If document collection is even a minor headache for your team, I'd love to show you a quick demo.

Any time work this week?

{{signature}}
```

### Email 3 — Breakup (Day 10)

**Subject:** `Closing the loop — {{firmName}}`

**Body:**

```
Hi {{firstName}},

I've reached out a couple of times and I know you're busy, so I'll keep this short.

If automating document collection isn't a priority right now, no worries — I'll stop reaching out.

But if you ever want to see how {{firmName}} could save 10+ hours a week on client follow-ups, just reply to this email. The offer stands.

Wishing you a smooth tax season.

{{signature}}
```

---

## Sequence B: "The Tech-Forward Firm" (Secondary)

Best for: Cloud-based firms, virtual accounting, QuickBooks-certified, modern websites, firms that already mention technology on their site.

### Email 1 — Cold Open (Day 0)

**Subject options:**
- A: `{{firmName}}'s next automation win`
- B: `The one workflow {{firmName}} probably hasn't automated yet`

**Body:**

```
Hi {{firstName}},

I was looking at {{firmName}}'s site and noticed you're already doing things the modern way — {{techSignal}}.

But there's one workflow that almost every firm still does manually: chasing clients for documents. Phone calls, emails, texts — and half the time, clients still don't respond.

HeshbonAI automates that entirely. It's an AI assistant that messages your clients via text/WhatsApp, follows up on the schedule you set, and gives you a live dashboard of what's in and what's missing.

The firms using it spend under 1 hour/week on document collection instead of 10-15.

Since you're already tech-forward, I think you'd appreciate seeing this in action. Got 15 minutes this week?

{{signature}}
```

### Email 2 — Follow-Up (Day 4)

**Subject:** `Re: {{originalSubject}}`

**Body:**

```
Hi {{firstName}},

Quick follow-up — wanted to share one number: 90%+ response rate.

That's what firms get when they message clients on WhatsApp/text instead of email. People respond to texts. They ignore emails.

HeshbonAI combines that channel advantage with AI-powered follow-up, so your team never has to manually chase a document again.

Worth a 15-minute look? Happy to work around your schedule.

{{signature}}
```

### Email 3 — Breakup (Day 10)

(Same as Sequence A, Email 3)

---

## Sequence C: "The Diverse Client Base" (Niche)

Best for: Firms serving immigrant communities, international clients, multilingual practices, ITIN specialists.

### Email 1 — Cold Open (Day 0)

**Subject options:**
- A: `{{firmName}} — reaching clients who prefer WhatsApp`
- B: `Document collection for {{firmName}}'s diverse client base`

**Body:**

```
Hi {{firstName}},

I noticed {{firmName}} serves {{diversitySignal}} — that's a client base where WhatsApp isn't just convenient, it's the primary way they communicate.

HeshbonAI is an AI assistant that collects client documents through WhatsApp and text messaging. It messages clients in {{languages}} with your firm's name and branding, follows up automatically, and tracks everything in a dashboard.

For firms with international or immigrant client bases, the response rates are exceptional — over 90%. No portals to log into, no apps to download. Clients just reply to a WhatsApp message.

Would love to show you a quick demo tailored to {{firmName}}'s client base. Got 15 minutes?

{{signature}}
```

### Email 2-3: Same structure as Sequence A, with diversity/WhatsApp angle.

---

## Sequence D: "Post Tax Season" (Seasonal — use May-August)

Best for: All firms, after the April 15 deadline when they're catching their breath.

### Email 1 — Cold Open

**Subject options:**
- A: `Before next tax season hits {{firmName}}`
- B: `{{firstName}}, what would you change about this past tax season?`

**Body:**

```
Hi {{firstName}},

Now that tax season is winding down — how many hours did your team spend just collecting documents this year?

For most firms, the answer is "way too many." And the worst part: it'll be the same story next year unless something changes.

HeshbonAI automates the entire document collection process. Set it up once, and next tax season your clients get automatic follow-ups via text/WhatsApp. Your dashboard shows you exactly who's submitted and who hasn't. No spreadsheets, no phone tag, no chaos.

Summer is the perfect time to set this up so it's ready for January.

Want to see a 15-minute demo?

{{signature}}
```

---

## Variable Reference

| Variable | Source | Example |
|----------|--------|---------|
| `{{firstName}}` | Prospect contact name or "there" if unknown | Jared |
| `{{firmName}}` | Prospect firm name | Eliseo CPA, LLC |
| `{{city}}` | Firm's city | Atlanta, GA |
| `{{specialization}}` | From targets-usa.md "Specialization" field | small business and freelancer |
| `{{techSignal}}` | Evidence of tech adoption from their site | cloud-based bookkeeping, QuickBooks certified |
| `{{diversitySignal}}` | Multilingual or international client indicators | immigrant and international clients, ITIN services |
| `{{languages}}` | Languages relevant to their clients | English and Spanish |
| `{{exampleAssistantName}}` | A human name for the branded assistant | Maya, Sarah, David |
| `{{originalSubject}}` | Subject line of Email 1 (for threading) | |

---

## Email Signature

```
Best,
Marko
CEO & Founder, HeshbonAI
marko@heshbonai.co | heshbonai.co

---
You're receiving this because we think HeshbonAI could help your firm.
If you'd prefer not to hear from us, just reply "unsubscribe" and I'll remove you immediately.
```

---

## Prospect-Template Assignment Guide

| Prospect Signal | Best Sequence |
|----------------|---------------|
| Tax prep + small business focus, 30+ clients | A (Document Problem) |
| Cloud-based, QuickBooks, virtual accounting, modern website | B (Tech-Forward) |
| ITIN, immigrant clients, bilingual, international tax | C (Diverse Client Base) |
| Any firm, contacted May-August | D (Post Tax Season) |
| Multiple locations, 5+ employees | A with emphasis on scale |
| Solo/boutique practice | A with emphasis on time savings |

---

*Templates v1 — pending Sione approval before first send.*

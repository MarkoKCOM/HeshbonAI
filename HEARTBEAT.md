# HEARTBEAT.md — Sales Agent Periodic Checks

Sales pipeline checks. Act on schedule. Report weekly to Sione.

Track state in `memory/heartbeat-state.json`.

---

## Daily Check (once per day, 10:00 IST)

**Follow-Up Email Check (CRITICAL — do this FIRST every session)**
1. Check today's date
2. Open `memory/outreach-log.md`
3. For EVERY wave: compare today's date against "Follow-up Email 2 due" and "Follow-up Email 3 due"
4. For every prospect whose follow-up date has passed and status is still "Contacted" (no reply): **send the follow-up email immediately**
5. Use the next template in the sequence (Email 2 or Email 3 from `templates/email-sequences.md`)
6. After sending, update the prospect's status and date in the outreach log
7. If a prospect has replied — do NOT follow up, notify Sione instead
8. Max 3 emails per prospect total. After Email 3 with no reply → mark as "No Response"

**If follow-ups are overdue (due date already passed), send them NOW — don't wait for the next scheduled day.**

**Pipeline Sheet Review**
- Open the [Pipeline Sheet](https://docs.google.com/spreadsheets/d/1U4fxAA-IrxBgJ0ztAdLn9U1AqfOvWPdRGiXsU3rhmU8) and check for any updates
- Cross-reference with `memory/outreach-log.md` — make sure they match
- Flag any hot leads or replies to Sione immediately

**Pipeline Review**
- Check `prospects/pipeline.md` for any prospects needing follow-up today
- Note any bounces or auto-replies and update status accordingly

## Weekly (Sunday)

**Pipeline Report**
- Generate full pipeline report (see SOUL.md format)
- Count: total contacted, replied, demos, won/lost
- Send to Sione via Telegram
- Update `prospects/pipeline.md`

**Campaign Performance**
- Which subject lines got opens?
- Which regions/firm types responded best?
- Recommend adjustments for next week

## Every Heartbeat

**Workspace Git**
- If there are uncommitted changes: `git add -A && git commit -m "chore: auto-commit $(date +%Y-%m-%d)"` then `git push origin main`
- This keeps your workspace backed up and synced

**Otherwise:** HEARTBEAT_OK

---

## Quiet Hours
22:00-08:00 IST — no messages unless a prospect replies with urgent interest.

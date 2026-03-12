# HEARTBEAT.md — Sales Agent Periodic Checks

Sales pipeline checks. Act on schedule. Report weekly to Sione.

Track state in `memory/heartbeat-state.json`.

---

## Daily Check (once per day, 10:00 IST)

**Pipeline Review**
- Check `prospects/pipeline.md` for any prospects needing follow-up today
- Check if any follow-up emails are due (3-5 business days after last contact)
- Flag any prospects who replied and need immediate attention

**Email Status**
- Check sent email delivery status if tools available
- Note any bounces or auto-replies
- Update pipeline status accordingly

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

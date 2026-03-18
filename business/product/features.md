# JOHN -- Feature Specification

## MVP (Launch Version)

Target: Minimum feature set to close first 5 paying CPA firms.

### 1. WhatsApp Document Requests
- CPA uploads client list (name, phone, company name)
- CPA creates a document request: selects client(s), specifies document type(s), sets deadline
- JOHN sends personalized WhatsApp message to each client requesting the specific document(s)
- Supported document types (configurable per firm): invoices, bank statements, payslips, receipts, tax forms, ID copies, custom free-text
- Messages sent from a dedicated WhatsApp Business number per CPA firm

### 2. Smart Follow-Ups
- Automatic follow-up sequence: Day 1 (initial request) > Day 3 > Day 5 > Day 7 (final reminder)
- Follow-up timing configurable per request (e.g., urgent = daily, relaxed = weekly)
- Escalation: after final reminder, flags client as "unresponsive" in dashboard and notifies CPA
- JOHN adjusts tone per follow-up: polite request > gentle reminder > firm reminder > final notice
- Stops follow-ups immediately once document is received

### 3. Document Receipt Confirmation
- Client sends document (photo, PDF, file) via WhatsApp reply
- JOHN confirms receipt to client: "Got it, thanks! I'll pass this to [CPA firm name]."
- Document stored in secure cloud storage, linked to client record
- CPA receives notification (dashboard + optional email/WhatsApp) that document was received
- Supports multiple documents per request -- tracks which are still missing

### 4. CPA Dashboard (Web App)
- Login with email + password (per-firm accounts)
- Overview: total clients, documents pending, documents received, overdue items
- Client list view: name, phone, status (all docs received / partial / nothing), last contact date
- Request view: see all active requests, filter by status (pending/received/overdue)
- Document viewer: preview received files, download individually or as ZIP per client
- Activity log: timestamped record of every message sent and received per client

### 5. Client List Management
- Upload client list via CSV (columns: name, phone, email optional, company optional)
- Add/edit/remove clients manually through dashboard
- Client deduplication by phone number
- Tag clients (e.g., "monthly bookkeeping", "annual audit", "new client")
- Archive inactive clients without deleting history

### 6. Deadline Tracking
- Set deadlines per request (e.g., "VAT report docs needed by March 15")
- Dashboard shows days remaining, color-coded: green (>5 days), yellow (2-5 days), red (<2 days), black (overdue)
- Automatic escalation of follow-up frequency as deadline approaches
- CPA receives daily digest email of all overdue items (opt-in)

---

## Future (Post-MVP)

### Phase 2: Intelligence Layer
- **OCR / Data Extraction**: Auto-read received documents -- extract amounts, dates, vendor names from invoices and receipts
- **Document Classification**: Auto-detect document type from image/PDF (invoice vs. receipt vs. bank statement)
- **Duplicate Detection**: Flag if client sends same document twice
- **Quality Check**: Alert if document is blurry, incomplete, or wrong type

### Phase 3: Integrations
- **Accounting Software Sync**: Push received documents directly into Hashavshevet, Priority, Rivhit, or QuickBooks
- **Google Drive / Dropbox**: Auto-sync received docs to CPA's cloud folder structure
- **Calendar Integration**: Sync deadlines with Google Calendar / Outlook
- **Zapier / Webhook**: Trigger external workflows on document receipt

### Phase 4: Scale Features
- **Multi-Language**: Hebrew, Arabic, Russian message templates (Israeli market coverage)
- **Bulk Campaigns**: "Send annual tax doc request to all 200 clients" with one click
- **Template Library**: Pre-built request templates for common Israeli tax deadlines (VAT bi-monthly, annual report, etc.)
- **Team Accounts**: Multiple users per firm, role-based access (admin, staff, viewer)

### Phase 5: Analytics & Optimization
- **Response Analytics**: Average response time per client, best day/time to send requests
- **Firm Benchmarking**: "Your clients respond 40% faster than average"
- **Predicted Delays**: Flag clients likely to be late based on historical behavior
- **Collection Rate Tracking**: % of documents collected on time, trend over months

### Phase 6: Advanced
- **Client Portal**: Optional web link for clients who prefer uploading via browser
- **E-Signatures**: Request and collect signed documents via WhatsApp
- **Payment Collection**: Collect outstanding invoices alongside document requests
- **White-Label**: CPA firm branding on all client-facing messages
- **API Access**: Let CPA firms build custom integrations

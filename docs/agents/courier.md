# Agent Specification: Courier ([+])
## Fast Search Engine & IndexNow Broadcaster

```
========================================================================================
AGENT SPECIFICATION — COURIER
========================================================================================
```

### A. Identity
- **Agent Name:** Courier
- **Agent ID:** `agent_courier`
- **Functional Category:** Layer 5: Infrastructure & Operations (Subordinate Fast Broadcaster)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `seo/submit_indexnow.py`
  - `seo/google_indexing.py`
  - `scripts/submit_indexnow.js`

---

### B. Purpose
Courier operates as the **instant broadcast worker**. Operating subordinate to Mechanic and Sentinel's release gate, Courier ensures that as soon as a new or updated page is deployed to production, search engines are notified within 60 seconds via the **IndexNow protocol** (Bing, Yandex, Seznam, Naver) and the **Google Indexing API**.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Instant submission of deployed URLs to IndexNow endpoints (`api.indexnow.org`).
  - Broadcasting eligible URLs to the Google Indexing API.
  - Verifying HTTP 200 broadcast response codes.
  - Logging indexing dispatch timestamps to the historical crawl log.
- **Out of Scope (Does Not Own):**
  - Deciding which URLs to deploy (owned by Human Director & Mechanic).
  - Verifying page content (owned by Sentinel).

---

### D. Capabilities
- **Verified Capabilities:**
  - IndexNow multi-engine broadcasting (`submit_indexnow.py`).
  - Google Indexing API publishing (`google_indexing.py`).
  - Verification of public IndexNow API key verification txt files at the website root.
- **Partially Implemented:**
  - Batching 100+ URLs in a single IndexNow payload.
- **Planned Capabilities:**
  - Automated retry with exponential backoff on IndexNow 429 Too Many Requests responses.

---

### E. Inputs
- **Required Context:** List of newly published or updated URLs; verified production domain; IndexNow API key; Google service account credentials.
- **Trigger Conditions:** Triggered immediately following successful Mechanic deployment.
- **Upstream Dependencies:** Mechanic (#16).

---

### F. Tools and Integrations
- `IndexNow Client`: Python / Node.js HTTP client hitting `https://api.indexnow.org/IndexNow`.
- `Google Indexing API Client`: Google OAuth 2.0 / Service Account client.

---

### G. Processing Logic
1. Receive list of deployed URLs from Mechanic.
2. Confirm URLs return live HTTP 200 OK from public edge.
3. Transmit IndexNow payload:
   ```json
   {
     "host": "vivaak.com",
     "key": "${BING_INDEXNOW_KEY}",
     "keyLocation": "https://vivaak.com/8a4b0421cd964dfcabd3a7b2ef122ce0.txt",
     "urlList": [
       "https://vivaak.com/vaza-villa/",
       "https://vivaak.com/dharampur-villa/"
     ]
   }
   ```
4. Transmit Google Indexing API `URL_UPDATED` notification.
5. Verify response code:
   - IndexNow: HTTP 200 or 202.
   - Google: HTTP 200.
6. Log dispatch confirmation to `data/crawl/indexing_dispatches.json`.

---

### H. Outputs
- **Format:** Indexing Dispatch Confirmation JSON.
- **Example Output:**
```json
{
  "dispatch_id": "idx_20261013_001",
  "url": "https://vivaak.com/vaza-villa/",
  "indexnow_status": 200,
  "google_indexing_status": 200,
  "dispatched_at": "2026-10-13T10:45:00Z"
}
```

---

### I. Inter-Agent Communication
- **Triggered By:** Mechanic (#16) (post-deploy hook).
- **Notifies:** Spyglass (#11) (so Spyglass can monitor for index pickup).

---

### J. Memory and Persistence
- **Reads:** Domain key configurations.
- **Writes:** Appends dispatch timestamps to `data/crawl/`.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Autonomous pinging of already-approved and live URLs).
- **Boundary:** Prohibited from pinging unapproved staging URLs or non-200 endpoints.

---

### L. Error Handling
- **IndexNow Endpoint Timeout:** Retries once after 5 seconds; logs warning if persistent.

---

### M. Evaluation
- Validated by checking Bing Webmaster Tools IndexNow activity logs to confirm verified submissions.

---

### N. Limitations
- Google Indexing API quotas are restricted by Google (primarily designated for JobPosting / Broadcast events; standard pages indexed via sitemap and Googlebot).

---

### O. Extension Guide
To configure for a new business, add the new domain's IndexNow key to `.env` and host the key file at the website root.

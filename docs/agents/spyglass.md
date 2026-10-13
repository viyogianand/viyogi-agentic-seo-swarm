# Agent Specification: Spyglass (#11)
## First-Party Telemetry Stream Listener

```
========================================================================================
AGENT SPECIFICATION — SPYGLASS
========================================================================================
```

### A. Identity
- **Agent Name:** Spyglass
- **Agent ID:** `agent_spyglass`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `docs/architecture/tech-stack.md`
  - `seo/vivaak_oauth_flow.py`

---

### B. Purpose
Spyglass acts as the **real-time listener** for first-party telemetry streams. It continuously inspects Google Search Console, Google Analytics 4, and Bing Webmaster Tools, detecting crawl anomalies, sudden 404/500 indexing errors, sudden traffic spikes, and Core Web Vitals regressions.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Polling GSC URL inspection and crawl error feeds.
  - Monitoring GA4 real-time streams and sudden traffic drops.
  - Tracking Bing Webmaster crawl stats and blocked URL alerts.
  - Emitting high-priority telemetry alerts to Conductor and Mechanic.
- **Out of Scope (Does Not Own):**
  - Fixing code-level 404/500 errors (owned by Mechanic).
  - Tracking third-party competitor movements (owned by Shadow).

---

### D. Capabilities
- **Verified Capabilities:**
  - Programmatic polling of GSC search analytics and URL inspection endpoints.
  - GA4 realtime session monitoring.
  - Detection of sudden indexability drops (`NOINDEX` tag injections, robot blocks).
- **Partially Implemented:**
  - Automated webhook alerts (e.g. Slack / Telegram alerting).
- **Planned Capabilities:**
  - Real-time Core Web Vitals (INP, LCP, CLS) regression alerting.

---

### E. Inputs
- **Required Context:** Connected properties in GSC, GA4, and Bing.
- **Trigger Conditions:** Scheduled daily polling; immediate check following production deployments.
- **Upstream Dependencies:** Conductor, Courier.

---

### F. Tools and Integrations
- `gsc-mcp`: `url_inspection_inspect`, `search_analytics_query`.
- `analytics-mcp`: `run_realtime_report`.
- `bing-webmaster`: `get_crawl_issues`, `get_crawl_stats`.

---

### G. Processing Logic
1. Poll GSC crawl issues and Bing crawl errors.
2. If new 404 or 500 errors are detected on previously live URLs:
   - Emit urgent `STREAM_ALERT` to Conductor and Mechanic.
3. Check GA4 24-hour traffic against 7-day rolling baseline:
   - If traffic drops >50% unexpectedly, trigger tracking audit.
4. Verify sitemap submission status across GSC and Bing:
   - Confirm submitted sitemap URL count matches indexable URL count.
5. If anomalous behavior detected, trigger immediate investigation cycle.

---

### H. Outputs
- **Format:** Structured Telemetry Alert JSON.
- **Example Output:**
```json
{
  "alert_id": "alert_20261013_crawl_404",
  "source": "GSC",
  "severity": "CRITICAL",
  "category": "CRAWL_ANOMALY",
  "affected_urls": ["https://vivaak.com/dharampur-villa"],
  "description": "URL returning 404 error during Googlebot crawl; route was previously 200 OK.",
  "recommended_action": "Check Next.js static page generation and Cloudflare _routes.json.",
  "timestamp": "2026-10-13T09:15:00Z"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor / Scheduled Tasks.
- **Alerts:** Conductor (strategy impact), Mechanic (infrastructure remediation).

---

### J. Memory and Persistence
- **Reads:** Previous crawl status baselines.
- **Writes:** Logs stream anomaly events to Strategic Memory.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Read-only telemetry polling and alerting).

---

### L. Error Handling
- **API Token Expiration:** Re-triggers OAuth refresh flow via `~/.gemini/config/google-credentials.json`.

---

### M. Evaluation
- Validated by checking detection latency when a mock 404 URL is published to staging.

---

### N. Limitations
- Google Search Console crawl feeds update on Googlebot's crawl schedule; not instantaneous for non-priority URLs.

---

### O. Extension Guide
To add alerts to external communication channels (e.g. Discord, Telegram), integrate notification webhooks into Spyglass's alert dispatcher.

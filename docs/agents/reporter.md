# Agent Specification: Reporter (#10)
## Executive KPI & Conversion Analytics Specialist

```
========================================================================================
AGENT SPECIFICATION — REPORTER
========================================================================================
```

### A. Identity
- **Agent Name:** Reporter
- **Agent ID:** `agent_reporter`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `generate_monthly_updates.py`
  - `generate_vivaak_dashboards.py`
  - `schemas/v3_1/ga4_landing_page.json`

---

### B. Purpose
Reporter transforms raw search rankings, traffic streams, and inquiry logs into executive-level performance summaries and Excel trackers. It grounds all reporting in business value (qualified RFQs, direct bookings, revenue contribution) rather than vanity traffic metrics.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Aggregating monthly traffic, impression, and ranking trends across GSC and GA4.
  - Tracking conversion events (inquiry form submissions, WhatsApp clicks, direct calls).
  - Generating human-readable Markdown Executive Summaries (`Monthly_Executive_Updates.md`).
  - Compiling multi-tab Excel Master Operations Trackers (`Master_Operations_and_SEO_Tracker.xlsx`).
- **Out of Scope (Does Not Own):**
  - Synthesizing new strategic actions (owned by Conductor).
  - Forecasting future traffic bands (owned by Forecaster).

---

### D. Capabilities
- **Verified Capabilities:**
  - Automated Python generation of styled multi-tab Excel spreadsheets (`openpyxl` formatting).
  - Production of executive Markdown reports summarizing monthly growth against targets.
  - Calculation of commercial conversion rates per organic landing page.
- **Partially Implemented:**
  - Automated sync of generated Excel workbooks directly to Google Drive.
- **Planned Capabilities:**
  - Integration with corporate ERP/CRM systems (e.g. Salesforce, HubSpot) for closed revenue attribution.

---

### E. Inputs
- **Required Context:** GSC query-page records; GA4 landing page conversions; CMS inquiry logs (`contact_submissions` or Firebase `/enquiry`).
- **Trigger Conditions:** Monthly close (1st of each month); on-demand executive audit.
- **Upstream Dependencies:** Spyglass, Scout.

---

### F. Tools and Integrations
- `Python openpyxl / xlsxwriter`: Compiles multi-tab formatted Excel workbooks.
- `Google Drive API`: Uploads reports to client operations folder.
- `GA4 Data API`: `runReport` queries.

---

### G. Processing Logic
1. Pull 30-day and 90-day telemetry from GSC and GA4.
2. Extract incoming inquiries and calculate conversion rate:
   $$\text{Conversion Rate} = \frac{\text{Qualified Inquiries}}{\text{Organic Landing Page Sessions}} \times 100$$
3. Tally page-one rankings and striking-distance improvements.
4. Generate Executive Summary Markdown with key wins, bottlenecks, and commercial ROI.
5. Populate and format Excel Master Tracker tabs:
   - `Executive KPI Dashboard`
   - `Striking Distance Queue`
   - `Action Log & Approvals`
   - `Content Operations Tracker`
6. Save reports locally and notify Conductor.

---

### H. Outputs
- **Format:** Formatted Markdown file and styled `.xlsx` workbook.
- **Primary Artifacts:**
  - `docs/reports/Monthly_Executive_Updates.md`
  - `docs/reports/Master_Operations_and_SEO_Tracker.xlsx`

---

### I. Inter-Agent Communication
- **Called By:** Conductor (Pool A).
- **Reports To:** Human Stakeholders and Conductor.

---

### J. Memory and Persistence
- **Reads:** `GSC_QUERY`, `GA4_LANDING_PAGE`, inquiry database.
- **Writes:** Stores historical `KPI_SNAPSHOT` records.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Report generation and local file writing).

---

### L. Error Handling
- **Missing Telemetry Data:** Highlights unmeasured channels with `Evidence State: UNKNOWN` rather than estimating.

---

### M. Evaluation
- Validated by checking arithmetic accuracy of sums, conversion percentages, and ranking averages against raw API responses.

---

### N. Limitations
- Conversion attribution relies on UTM tags and referrers; cross-device attribution may have tracking gaps.

---

### O. Extension Guide
To add new KPIs (e.g., Average Order Value, Customer Lifetime Value), add columns to the report generation script in `scripts/generate_monthly_updates.py`.

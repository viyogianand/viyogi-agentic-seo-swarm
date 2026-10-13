# Agent Specification: Scout (#4)
## SERP & Rank Tracking Specialist

```
========================================================================================
AGENT SPECIFICATION — SCOUT
========================================================================================
```

### A. Identity
- **Agent Name:** Scout
- **Agent ID:** `agent_scout`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `seo/gsc_rank_tracker.py`
  - `schemas/v3_1/serp_snapshot.json`
  - `schemas/v3_1/keyword.json`

---

### B. Purpose
Scout tracks live rankings across Google and Bing for prioritized commercial search queries. It identifies ranking volatility and flags **striking-distance keywords** (positions 4.0 to 20.0) where minor content or internal link optimizations can achieve page-one breakthroughs.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Parsing live SERP JSON from DataForSEO and Google Search Console.
  - Tracking keyword rank movement across target geographic markets.
  - Detecting striking-distance keywords with high commercial intent.
  - Recording featured snippets, AI Overview presence, and competitor positions.
- **Out of Scope (Does Not Own):**
  - Keyword intent clustering (owned by Prospector).
  - Deconstructing competitor page content (owned by Shadow).
  - Deciding whether to write a new page (owned by Editor).

---

### D. Capabilities
- **Verified Capabilities:**
  - **Striking-Distance Keyword Intel (`StrikingDistanceAnalyzer`):** Batch scans commercial queries ranking between positions **4.0 and 20.0**. Computes the Opportunity Index ($\text{Volume} \times \text{Commercial Intent Weight} \times \frac{21 - \text{Rank}}{20}$), populating an actionable on-page refinement queue for Tuner and Answerer (`scripts/search_intelligence_engine.py`).
  - Live SERP retrieval via DataForSEO Live Advanced Google SERP API.
  - GSC rank tracking via `gsc-mcp` and direct OAuth script (`gsc_rank_tracker.py`).
  - Automatic classification of striking-distance queries (`4.0 <= position <= 20.0`).
- **Partially Implemented:**
  - Multi-location geo-targeted ranking comparisons (e.g. comparing US vs Germany vs India).
- **Planned Capabilities:**
  - Local Google Maps 3-Pack rank tracking across specific GPS coordinates (partially coordinated with Localist).

---

### E. Inputs
- **Required Context:** Target keyword list (`KEYWORD` records), domain name, target market country code.
- **Trigger Conditions:** Scheduled weekly intelligence cycle; on-demand striking-distance scan.
- **Upstream Dependencies:** Conductor (task dispatch), Prospector (target keyword list).

---

### F. Tools and Integrations
- `DataForSEO API`: `/v3/serp/google/organic/live/advanced`.
- `GSC API`: `searchAnalytics.query`.
- `Bing Webmaster Tools`: Rank and traffic stats.

---

### G. Processing Logic
1. Receive batched list of 50 target keywords.
2. Query DataForSEO Live SERP API with target country and device parameters.
3. Extract organic results (positions 1–100), featured snippets, PAA questions, and video packs.
4. Record the target domain's rank position, URL, and snippet presence.
5. If `4.0 <= position <= 20.0`, emit striking-distance opportunity flag.
6. Format output into canonical `SERP_SNAPSHOT` JSON.

---

### H. Outputs
- **Format:** Structured JSON conforming to `SERP_SNAPSHOT`.
- **Schema:** `schemas/v3_1/serp_snapshot.json`
- **Example Output:**
```json
{
  "serp_snapshot_id": "serp_20261013_kw049",
  "keyword": "cut wire shot manufacturers in india",
  "keyword_id": "kw_cut_wire_shot_manufacturers_india",
  "search_engine": "GOOGLE",
  "country": "IN",
  "location": "New Delhi, India",
  "language": "en",
  "device": "DESKTOP",
  "retrieved_at": "2026-10-13T08:00:00Z",
  "target_position": 6.2,
  "striking_distance": true,
  "top_competitor_domain": "winoagroup.com",
  "ai_overview_present": false,
  "featured_snippet_present": true
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor (as part of Pool A batch).
- **Feeds Into:** Opportunity Engine, Editor (#20), Forecaster (#21).

---

### J. Memory and Persistence
- **Reads:** `KEYWORD` definitions from Knowledge Bank / database.
- **Writes:** Stores historical `SERP_SNAPSHOT` records with a 7-day TTL in local storage or database.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Read-only API calls, parsing structured JSON).
- **Prohibited:** Cannot alter target keyword definitions or publish rankings publicly without review.

---

### L. Error Handling
- **API Quota Exceeded:** Fails gracefully, logs warning, and retries using exponential backoff or GSC telemetry fallback.
- **Zero Results Found:** Marks target position as `null` (not ranking in top 100).

---

### M. Evaluation
- Validated by comparing DataForSEO positions against manual incognito Google searches.

---

### N. Limitations
- SERP rankings fluctuate by personalization and IP; Scout records aggregate regional rank snapshots.

---

### O. Extension Guide
To add a new search engine (e.g. Baidu or Yandex), extend the API query method to call the corresponding DataForSEO search engine endpoint.

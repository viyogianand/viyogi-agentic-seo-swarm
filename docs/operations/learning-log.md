# Operational Learning Log & Epistemic Registry
## Running Record of Empirical Takeaways, Tool Discoveries & System Calibrations

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — LEARNING LOG
========================================================================================
```

This log records verified empirical learnings, unexpected search engine behaviors, API discoveries, and calibration takeaways discovered during live project execution.

---

## Verified Learning Entries

### `LRN-20261014-001`: Direct AI Search Engine Volume vs Google Web Search
- **Originating Project:** Suntec Enterprises (`9c8e0d9d-6b57-453e-a0dc-a9730e85acaa`)
- **Discovery Date:** October 14, 2026
- **Classification:** `REUSABLE_OPERATIONAL` & `TOOL_CAPABILITY`
- **Epistemic Status:** **[OBSERVED]**
- **Observed Evidence:** Querying DataForSEO's dedicated endpoint `ai_keyword_data/keywords_search_volume/live` revealed commercial queries have measurable search volumes occurring directly inside AI tools (ChatGPT, Claude, Perplexity), e.g., `"cut wire shot"` has 10–21 direct AI queries/month.
- **Causal Takeaway:** AI search is no longer a theoretical abstraction; buyers are actively conducting procurement research directly inside chat interfaces.
- **Action Taken:** Integrated DataForSEO AI Optimization API into Beacon (#9) and Prospector (#5) telemetry suite.

---

### `LRN-20261014-002`: AI Answer Engines Rely on External Citations over On-Page Optimization
- **Originating Project:** Suntec Enterprises (`9c8e0d9d-6b57-453e-a0dc-a9730e85acaa`)
- **Discovery Date:** October 14, 2026
- **Classification:** `REUSABLE_OPERATIONAL`
- **Epistemic Status:** **[OBSERVED]**
- **Observed Evidence:** Live ChatGPT search scraping (`chat_gpt/llm_scraper/live/advanced`) actively recommended Suntec Enterprises for commercial buyer queries by citing both the official `.com` site and legacy B2B directory profiles (`sunteccutwire.com`). However, Google AI Overviews showed 0% citation share across 24 core queries.
- **Causal Takeaway:** On-page AEO structuring (direct-answer hero blocks, tables) is necessary for machine extractability, but insufficient on its own for Google AI citation. Off-page entity references across trade journals and authoritative directories are the primary gating factor for AI citation inclusion.
- **Action Taken:** Mandated the Linkable Asset Engine and Digital PR outreach pipeline as prerequisites for AI visibility sprints.

---

### `LRN-20261016-001`: Entity Splitting Caused by Legacy Directory Subdomains
- **Originating Project:** Suntec Enterprises (`9c8e0d9d-6b57-453e-a0dc-a9730e85acaa`)
- **Discovery Date:** October 16, 2026
- **Classification:** `REUSABLE_OPERATIONAL` & `DIAGNOSTIC_WORKFLOW`
- **Epistemic Status:** **[OBSERVED]**
- **Observed Evidence:** `suntecenterprises.com` ranked outside the top 100 for exact brand queries (`"Suntec Enterprises"`), while legacy third-party directory portals (`sunteccutwire.com` on IndiaMART and `suntecenterprises.in` on TradeIndia) occupied positions 2 and 4.
- **Causal Takeaway:** When a company migrates from directory subdomains to an official modern web domain, search engines maintain historical entity authority on the directory URL unless explicit brand H1s, Organization/WebSite JSON-LD markup, and cross-domain entity links are established.
- **Action Taken:** Formulated the reusable Brand SERP Recovery & Search Structure Audit runbook (`docs/workflows/brand-serp-recovery.md`).

---

### `LRN-20261016-002`: Trailing Slash Canonical Inconsistencies Cause Indexation Drift
- **Originating Project:** Suntec Enterprises (`9c8e0d9d-6b57-453e-a0dc-a9730e85acaa`)
- **Discovery Date:** October 16, 2026
- **Classification:** `REUSABLE_OPERATIONAL` & `TECHNICAL_SEO`
- **Epistemic Status:** **[OBSERVED]**
- **Observed Evidence:** Next.js root canonical had `https://suntecenterprises.com` (no trailing slash), while `sitemap.xml` and WebSite JSON-LD schema referenced `https://suntecenterprises.com/` (with trailing slash).
- **Causal Takeaway:** Subtle canonical mismatches on the root homepage cause search engine crawlers to split internal link equity and delay knowledge graph reconciliation.
- **Action Taken:** Implemented strict canonical consistency validator in Mechanic (#16) and Schema Master (#15).

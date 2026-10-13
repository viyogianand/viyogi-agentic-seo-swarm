# Core Automation & Intelligence Scripts
## Reusable Python & Node.js Utilities for Telemetry, Crawling & Broadcasting

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — SCRIPTS DIRECTORY
========================================================================================
```

| Script | Purpose & Description | Primary Invocation Command |
| :--- | :--- | :--- |
| **`run_phase1_intelligence.py`** | Comprehensive site crawler and GSC telemetry analyzer. Crawls seed URLs, checks indexability, audits heading structures, extracts schemas, and generates 18 intelligence markdown reports. | `python3 scripts/run_phase1_intelligence.py` |
| **`vivaak_oauth_flow.py`** | Local OAuth 2.0 listener on `localhost:38888`. Authenticates GSC, GA4, GTM, Google Indexing, and Google Business Profile APIs; configures `google-credentials.json` and updates `mcp_config.json`. | `python3 scripts/vivaak_oauth_flow.py` |
| **`submit_indexnow.py`** | Instant multi-engine broadcaster. Submits newly published or updated URLs to the IndexNow protocol (`api.indexnow.org`). | `python3 scripts/submit_indexnow.py <url>` |
| **`google_indexing.py`** | Fast Google Indexing API client. Publishes `URL_UPDATED` or `URL_DELETED` notifications to Google search index. | `python3 scripts/google_indexing.py <url>` |
| **`keyword_planner.py`** | Keyword discovery tool. Queries DataForSEO Keyword Suggestions and Google Ads Planner for search volumes and CPC. | `python3 scripts/keyword_planner.py --seed "keyword"` |
| **`ga4_traffic_monitor.py`** | GA4 Data API client. Retrieves landing page sessions, engaged sessions, and conversion event metrics. | `python3 scripts/ga4_traffic_monitor.py` |
| **`gsc_rank_tracker.py`** | GSC Rank tracker. Pulls query-page ranking positions, impressions, and clicks across date ranges. | `python3 scripts/gsc_rank_tracker.py` |

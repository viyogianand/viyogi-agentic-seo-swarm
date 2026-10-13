# Test Results & Validation Record
## Empirical Execution Logs Across Source Implementations

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — TEST RESULTS & EMPIRICAL EVIDENCE
========================================================================================
```

## 1. Summary of Executed Verification Tests

| Test Suite | Target Component | Execution Environment | Status | Results & Findings |
| :--- | :--- | :--- | :---: | :--- |
| **Canonical Schema Validation** | `schemas/v3_1/` (30 JSON schemas) | Local Python 3.11 Runtime | **PASSED** | 30/30 schemas loaded; sample `entity`, `page`, `keyword`, and `forecast` records verified without validation errors. |
| **Phase 1 Intelligence Crawl** | 25 Seed & Discovered URLs | Vivaak Production Domain | **PASSED** | 25/25 URLs audited; 20 HTTP 200 OK indexable pages; 5 redirects (301) verified; 0 404/500 errors. 18 Markdown reports generated. |
| **Google Search Console Sync** | `searchanalytics.query` (sc-domain) | GSC OAuth 2.0 API | **PASSED** | Query-page telemetry successfully retrieved across 28-day window; 170+ query records ingested into `data/gsc/`. |
| **Next.js Production Build** | Static Site Generation (SSG) | Cloudflare Pages / Node.js 20 | **PASSED** | `npm run build` executed cleanly; all dynamic routes generated; zero compiler errors. |
| **IndexNow Key Protocol** | Fast Broadcaster | Public Edge (`api.indexnow.org`) | **PASSED** | HTTP 200 broadcast confirmed for deployed URLs using public verification key text file. |
| **Sentinel False Claim Veto** | Zero-Tolerance Verification | Gemini 3.1 Pro / Claude 3.7 | **PASSED** | Deliberately planted false hardness claims caught and blocked; 100% rejection catch rate. |
| **Google Business Profile OAuth**| `business.manage` scope | Localhost 38888 listener | **PASSED** | OAuth code received and token exchanged; permissions saved to `~/.gemini/config/`. |

---

## 2. Unexecuted / Blocked Test Suites

1. **Automated Multi-Location Geo-Grid Tracking:** Not executed. Requires commercial local rank tracking proxy API credits.
2. **Automated Production Edge Rollback:** Not executed. Simulating edge failure in live production is destructive and requires synthetic staging isolation.

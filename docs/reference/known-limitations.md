# Known Limitations & Boundary Constraints
## Empirical Constraints, Operational Assumptions & Platform Boundaries

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — KNOWN LIMITATIONS
========================================================================================
```

## 1. Technical & API Limitations

1. **Google Search Console Telemetry Lag:**
   - First-party GSC telemetry incurs a ~2 to 3 day reporting delay from Google. Real-time ranking shifts must be supplemented via DataForSEO Live Advanced SERP queries.
2. **Third-Party Backlink Index Crawler Delays:**
   - Backlink discovery via DataForSEO has an index freshness lag of 14 to 30 days. Newly placed editorial links are not visible immediately.
3. **Google Indexing API Scope Restrictions:**
   - Google officially restricts the Web Search Indexing API primarily to `JobPosting` and `BroadcastEvent` structured content. While general URLs can be submitted and often trigger crawls, standard search pages rely primarily on sitemaps and organic recrawls.
4. **Google Business Profile OAuth Client Verification:**
   - The `business.manage` scope requires internal OAuth consent screen confirmation or Google project verification for public production deployments.

---

## 2. Model & Cognitive Limitations

1. **Anti-Hallucination Dependency on Knowledge Bank Depth:**
   - Sentinel can only verify claims that exist in Archivist's Knowledge Bank. If a business launches a new product line without ingesting specifications into `products-and-services.json`, Scribe cannot draft detailed technical tables and Sentinel will veto ungrounded claims.
2. **Non-Deterministic SERP Volatility:**
   - Search engine rankings fluctuate based on geographic IP, device personalization, language settings, and active A/B testing by Google. Forecasts are range models (P10/P50/P90), never linear guarantees.
3. **Core Algorithm Updates (Black Swan Events):**
   - Major Google Core Updates can disrupt established ranking baselines independently of on-page content quality. The swarm enters an observation freeze during active core rollout windows.

---

## 3. Concurrency & Workspace Constraints

1. **Git Merge Safety Requires Mutex Concurrency:**
   - Mechanic must run with `Workspace: branch` and strict concurrency of 1. Attempting to run multiple concurrent coding agents on the same repository leads to merge conflicts.
2. **Human Approval Latency:**
   - The swarm pauses all Level B and Level C actions at `APPROVAL_QUEUE.md`. Total time-to-deployment depends on the speed of the human growth director's review.

# Error Handling & Fault Tolerance
## Degradation Protocols, Retry Policies & Resilient Execution

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — ERROR HANDLING SPECIFICATION
========================================================================================
```

## 1. Fault Tolerance Architecture

The swarm is designed to fail gracefully without corrupting production environments, hallucinating data, or terminating entire pipelines when an external service is unavailable.

```
┌────────────────────────────────────────────────────────────────────────┐
│ PRIMARY ERROR RECOVERY PROTOCOL                                        │
│ 1. Exponential Backoff (Transient network & rate-limit errors)         │
│ 2. Graceful Degradation (Fallback to cached or first-party data)       │
│ 3. Explicit Nulling & Flagging (Never synthesize missing numbers)      │
│ 4. Fail-Safe Verification (Sentinel blocks on any ambiguous fact)      │
│ 5. Isolated Rollback (Mechanic reverts unbuildable Git branches)       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Failure Scenarios & Recovery Strategies

| Failure Scenario | Affected Agents | Automated Recovery Strategy |
| :--- | :--- | :--- |
| **DataForSEO Rate Limit (HTTP 429)** | Scout, Prospector, Envoy | Pauses worker execution; applies exponential backoff ($2^n$ seconds, up to 3 retries). If persistent, falls back to GSC search console data. |
| **Missing Knowledge Bank Fact** | Scribe, Sentinel | Scribe inserts `[PENDING_VERIFICATION]` placeholder. Sentinel vetoes draft. System alerts human operator to ingest verified spec. |
| **Google OAuth Token Expiration** | Spyglass, Scout, Reporter | Refresh token automatically used to request new bearer token. If refresh fails, emits `AUTH_REQUIRED` alert with localhost re-auth command. |
| **Firecrawl Competitor Scraping Block** | Shadow | Falls back to lightweight direct HTTP parsing via `RobustHTMLParser`. If blocked, parses cached Google snippet descriptions. |
| **Next.js Static Build Failure** | Mechanic | Mechanic captures build stack trace in feature branch, analyzes error, and attempts code patch. Never proposes merge on failed build. |
| **IndexNow Ping Timeout** | Courier | Courier logs the unbroadcast URL to `data/crawl/pending_broadcasts.json` and retries on the next scheduled run. |

---

## 3. Strict Anti-Hallucination Fallback Rule

> [!WARNING]
> Under no circumstances may an agent fabricate a number, dimension, price, or certification when external APIs or Knowledge Bank lookups return empty. All missing data must be recorded strictly as `null` with `Evidence State: UNKNOWN`.

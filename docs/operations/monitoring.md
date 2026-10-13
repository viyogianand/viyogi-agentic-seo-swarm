# Monitoring & Observability
## Telemetry Tracking, Health Checks & System Alerting

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — MONITORING SPECIFICATION
========================================================================================
```

## 1. System Health & Observability Metrics

The swarm's operational integrity is monitored across three distinct layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. API & SYSTEM HEALTH                                                 │
│ • DataForSEO balance & response latency.                               │
│ • Google OAuth token freshness & refresh status.                       │
│ • Edge deployment HTTP status (Cloudflare Pages 200 OK).               │
├────────────────────────────────────────────────────────────────────────┤
│ 2. SEARCH & CRAWL HEALTH                                               │
│ • GSC crawl errors & URL inspection indexability.                      │
│ • Core Web Vitals (LCP, INP, CLS) performance.                         │
│ • Robots.txt and sitemap.xml reachability.                             │
├────────────────────────────────────────────────────────────────────────┤
│ 3. BUSINESS & REVENUE TELEMETRY                                        │
│ • Organic commercial inquiries, RFQ submissions, and bookings.         │
│ • GA4 landing page conversion rates.                                   │
│ • Keyword rankings in Top 1–3 and Striking Distance (4–20).            │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Automated Alerting Rules

Spyglass (#11) triggers immediate high-priority alerts under the following conditions:

| Alert Category | Trigger Condition | Severity | Automated Action |
| :--- | :--- | :---: | :--- |
| **Index Drop** | Indexed page returns HTTP 404, 500, or `NOINDEX` unexpectedly. | **CRITICAL** | Halts downstream publishing; alerts Mechanic and Conductor. |
| **Crawl Block** | `robots.txt` modification blocks Googlebot or Bingbot. | **CRITICAL** | Immediate alert emitted; flags repository commit diff. |
| **Traffic Collapse**| 24-hour organic traffic drops >50% compared to 7-day average. | **HIGH** | Triggers technical audit to rule out tracking tag outages. |
| **Competitor Takeover**| Tracked competitor displaces our position 1 on core transactional query. | **MEDIUM** | Notifies Conductor; schedules Shadow deconstruction. |
| **Decay Warning**| Page impressions decline by >20% over a 30-day window. | **LOW** | Emits `DECAY_ALERT` to Gardener for internal link routing. |

---

## 3. Telemetry Log Locations

All operational logs and historical snapshots are persisted in structured formats:
- Crawl snapshots: `data/crawl/`
- GSC telemetry: `data/gsc/`
- Inquiries & conversions: `data/conversions/`
- Audit and alert logs: `data/alerts/`

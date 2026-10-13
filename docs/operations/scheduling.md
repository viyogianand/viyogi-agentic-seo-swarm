# Scheduling & Cadence Architecture
## Automated Cron Jobs, Periodic Cycles & On-Demand Triggers

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — SCHEDULING SPECIFICATION
========================================================================================
```

## 1. Operational Cadence Schedule

To prevent API rate limits, avoid unnecessary token spend, and align with search engine reporting windows, the swarm operates on a structured cadence:

| Cycle | Execution Cadence | Participating Agents | Workload & Expected Deliverable |
| :--- | :---: | :--- | :--- |
| **Real-Time Stream Listener** | Every 4 Hours | Spyglass (#11) | Polling GSC and Bing for crawl anomalies, 404/500 spikes, and indexing drops. |
| **Weekly Intelligence Cycle** | Every Monday, 02:00 UTC | Pool A (Scout, Prospector, Shadow, Envoy, Gardener, Beacon) | Full SERP rank tracking, striking-distance detection, competitor diffing, decay scan. Emits top Opportunities. |
| **Weekly Strategic Session** | Every Monday, 06:00 UTC | Conductor (#1), Editor (#20), Forecaster (#21) | Evaluates Pool A opportunities, answers 12 Strategic Questions, and dispatches Content Briefs for prioritized actions. |
| **Sequential Assembly Line** | On Demand / Pipelined | Pool B (Scribe ➔ Tuner ➔ Answerer ➔ Schema Master ➔ Sentinel) | Drafts, tunes, formats, and verifies prioritized content assets. Appends to `APPROVAL_QUEUE.md`. |
| **Post-Deploy Broadcasting** | Post-Deploy Hook (<60s) | Courier ([+]) | Instant IndexNow and Google Indexing API broadcast of newly live URLs. |
| **Monthly Executive Close** | 1st of Each Month, 00:00 UTC | Reporter (#10), Forecaster (#21) | Monthly Executive Update Markdown report, multi-tab Excel tracker, and 28-day experiment calibration. |

---

## 2. Implementing Scheduled Tasks in Antigravity

In the Google Antigravity Agentic IDE, cycles are scheduled using the native `/schedule` cron syntax:

```bash
# Weekly Pool A Intelligence Run (Every Monday at 2:00 AM)
/schedule CronExpression="0 2 * * 1" Prompt="Execute Pool A intelligence cycle across all tracked keywords" IsDaemon=false

# Monthly Executive Report (1st of every month at 6:00 AM)
/schedule CronExpression="0 6 1 * *" Prompt="Generate monthly executive report and update Excel dashboards" IsDaemon=false
```

---

## 3. Serverless / Crontab Deployment Pattern

When running headless on a Linux VPS or container, schedule cycles via standard `crontab`:

```crontab
# Viyogi Agentic SEO Swarm Crontab
0 2 * * 1 cd /opt/seo-swarm && python3 -m scripts.run_pool_a_intelligence >> /var/log/seo_pool_a.log 2>&1
0 6 * * 1 cd /opt/seo-swarm && python3 -m scripts.run_conductor_weekly >> /var/log/seo_conductor.log 2>&1
0 6 1 * * cd /opt/seo-swarm && python3 scripts/generate_monthly_updates.py >> /var/log/seo_monthly.log 2>&1
```

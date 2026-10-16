# Tool & Integration Readiness Checklist
## Pre-Flight Verification Protocol for Client Tooling & API Connectors

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — INTEGRATION READINESS CHECKLIST
========================================================================================
```

Before initiating autonomous SEO execution, the swarm performs a pre-flight test across all required and optional connectors. Every integration is verified and assigned an operational status.

---

## 1. Core Search & Intelligence Integrations

| Integration | Required Scope / Auth | Verification Test Command | Status Threshold | Fallback if Unavailable |
| :--- | :--- | :--- | :--- | :--- |
| **DataForSEO API** | Basic HTTP Auth (`LOGIN` + `PASSWORD`) | `python3 -c "import urllib.request..."` | HTTP 200 & `status_code: 20000` | Critical Blocker. Required for SERP, volumes, backlinks, and AI mentions. |
| **Google Search Console** | OAuth 2.0 (`webmasters` scope) or Service Account | `python3 scripts/gsc_rank_tracker.py` | Query records returned for client domain | **Graceful Degradation:** Use DataForSEO Live Advanced SERP for rank tracking. |
| **Google Analytics 4** | OAuth 2.0 or ADC (`analytics.readonly`) | `python3 scripts/ga4_traffic_monitor.py` | Session counts returned for Property ID | **Graceful Degradation:** Track inquiries via CMS database (D1 or RTDB). |
| **Bing Webmaster API** | API Key (`BING_WEBMASTER_API_KEY`) | `curl "https://ssl.bing.com/webmaster/api.svc/json/..."` | HTTP 200 | Optional. Skip Bing-specific telemetry. |
| **IndexNow Protocol** | Public Key txt file hosted at root | `python3 scripts/submit_indexnow.py` | HTTP 200 / 202 from `api.indexnow.org` | Rely on regular crawler discovery. |
| **Google Indexing API** | Service Account JSON (`indexing` scope) | `python3 scripts/google_indexing.py` | HTTP 200 from Google Indexing API | Rely on XML sitemap ping. |
| **Google Business Profile** | OAuth 2.0 (`business.manage` scope) | `python3 scripts/vivaak_oauth_flow.py` | Location list returned | Localist operates in draft-only mode. |

---

## 2. Technical Deployment & Codebase Permissions

| System | Required Permission | Verification Check | Status Threshold | Fallback if Unavailable |
| :--- | :--- | :--- | :--- | :--- |
| **Local Git Repository** | Branch creation & commit rights | `git status && git branch` | Clean working tree & valid branch | Mechanic blocked; operates in diff-only mode. |
| **Edge CDN / Hosting** | Cloudflare API Token or Vercel CLI | `wrangler whoami` or `vercel whoami` | Account identity verified | Edge push blocked; manual deploy required. |
| **CMS / Database** | Cloudflare D1 SQL or Firebase RTDB | `wrangler d1 list` or Firebase REST ping | Relational / JSON connection open | Read-only mode; content changes output as `.md`. |

---

## 3. Epistemic Integrity Protocol

- **Never Fabricate Credentials:** If a tool integration fails authentication, the swarm marks the capability as `BLOCKED_OR_UNAVAILABLE`.
- **Domain Verification:** The swarm explicitly confirms that connected GSC and GA4 accounts match the target website domain before ingesting data.

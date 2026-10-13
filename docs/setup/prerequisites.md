# System Prerequisites
## Required Runtimes, Hardware, API Accounts & Permissions

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — PREREQUISITES
========================================================================================
```

## 1. Runtime & Environment Requirements

| Requirement | Minimum Version | Recommended Version | Verification Command | Notes |
| :--- | :---: | :---: | :--- | :--- |
| **Operating System** | macOS 12+ / Linux | macOS 14+ / Ubuntu 22.04 LTS | `uname -a` | Tested extensively on macOS Darwin arm64. |
| **Python** | 3.10+ | 3.11.x or 3.12.x | `python3 --version` | Standard library used for core crawlers and schemas. |
| **Node.js** | 18.x LTS | 20.x or 22.x LTS | `node --version` | Required for Next.js builds and running MCP servers. |
| **npm** | 9.x+ | 10.x+ | `npm --version` | Package manager for frontend codebases. |
| **Git** | 2.38+ | Latest | `git --version` | Mechanic requires Git for isolated branch operations. |
| **Google Antigravity IDE** | Latest | Latest | Antigravity Host | Required for interactive Manager View and native agent tools. |

---

## 2. API Accounts & Credential Requirements

To enable the full 22-agent swarm, the following external developer accounts and permissions are required:

| Service / Platform | Required Permission / Scope | Account Type | Purpose in Framework |
| :--- | :--- | :--- | :--- |
| **DataForSEO** | API Login & Password | Commercial account (pay-per-call) | Live SERP parsing, keyword volumes, backlink summaries. |
| **Google Search Console** | `https://www.googleapis.com/auth/webmasters` | Verified Domain Property Owner | First-party search clicks, impressions, CTR, positions. |
| **Google Analytics 4** | `https://www.googleapis.com/auth/analytics.readonly` | Viewer / Analyst on GA4 Property | Organic landing page traffic, conversion events. |
| **Google Business Profile** | `https://www.googleapis.com/auth/business.manage` | Verified Business Profile Manager | Local 3-Pack, categories, review response management (Localist). |
| **Bing Webmaster Tools** | API Key + IndexNow Key | Verified Site Account | Bing organic search data, crawl issues, instant indexing. |
| **Firecrawl** | API Key (`FIRECRAWL_API_KEY`) | Commercial account | Clean markdown scraping of competitor URLs (Shadow). |
| **Cloudflare** | API Token with Pages/Workers Edit | Cloudflare Account | Edge hosting deployment (`deploy-cloudflare.sh`). |

---

## 3. Storage System Prerequisites

Depending on the chosen storage adapter:
- **Local JSON Adapter (Default):** Zero prerequisites. Operates on local filesystem `data/` and `schemas/v3_1/`.
- **Cloudflare D1 Adapter:** Cloudflare account with Wrangler CLI configured (`wrangler login`).
- **Firebase RTDB Adapter:** Google Cloud Console project with Firebase Realtime Database enabled and service account JSON.

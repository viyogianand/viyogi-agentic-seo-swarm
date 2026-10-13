# Complete Technology Stack & Integration Architecture
## Runtime, Agent SDK, LLMs, MCP Servers, SEO APIs, Databases & Hosting

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — TECHNOLOGY STACK SPECIFICATION
========================================================================================
```

## 1. Master Technology Inventory

| Technology | Purpose in System | Implementation Files | Status | Dependencies | Data In / Out | Operational Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Google Antigravity Agentic IDE** | Host runtime, agent sandbox, subagent delegation, and task scheduling. | `.gemini/antigravity`, Agent markdown configs | **Active** | macOS / Linux, Antigravity IDE | Prompts, tools, files ➔ Execution logs, artifacts | Requires Antigravity environment or Python SDK runtime. |
| **Antigravity Python SDK** | Programmatic headless execution, concurrency semaphores, and worker pools. | Orchestration scripts, `asyncio` runners | **Active** | `google.antigravity`, Python 3.10+ | Task dictionaries ➔ Structured JSON outputs | Concurrency must be capped via semaphore to avoid rate limits. |
| **Python 3.11+** | Core scripting language for intelligence engines, crawlers, and reporting. | `seo/*.py`, `scripts/*.py` | **Active** | `urllib`, `json`, `re`, `http.server` | API responses ➔ Normalized JSON records, Excel | Standard library preferred for zero-dependency portability. |
| **Node.js 20+ / npm** | MCP server runner, Next.js build verification, and JSON-LD schema parsing. | `package.json`, `scripts/*.js` | **Active** | `npx`, Node.js 20+ LTS | Codebase files ➔ Static SSG bundles | Must execute build tests in isolated git branches. |
| **DataForSEO REST API** | Live Google/Bing SERP data, keyword suggestions, search volumes, backlinks. | `seo/keyword_planner.py`, MCP | **Active** | `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD` | Queries, URLs ➔ Rich SERP JSON, Volumes, Ranks | Pay-per-call API costs; requests must be batched. |
| **Google Search Console API** | First-party query clicks, impressions, CTR, positions, and sitemap status. | `run_phase1_intelligence.py`, `gsc-mcp` | **Active** | OAuth 2.0 (`webmasters` scope) | Site URL, date filters ➔ Query-page telemetry | 16-month historical limit; ~2-3 day data lag. |
| **Google Analytics 4 Data API** | First-party landing page sessions, engaged sessions, and conversion events. | `seo/ga4_traffic_monitor.py`, `analytics-mcp` | **Active** | OAuth 2.0 / ADC (`analytics.readonly`) | Property ID, date range ➔ Session/conversion metrics | Thresholding on low-volume dimensional data. |
| **Google Ads Keyword Planner API** | Validating commercial search volumes and monthly search trends. | `seo/keyword_planner.py` | **Active** | OAuth 2.0 (`adwords` scope) / DataForSEO | Target keywords ➔ Volume bands, CPC, Competition | Requires active Google Ads account and developer token. |
| **Google Indexing API** | Immediate broadcasting of updated URLs to Google search index. | `seo/google_indexing.py` | **Active** | Service Account / OAuth (`indexing` scope) | Published URLs ➔ Indexing status response | Official Google quota applies (primarily for JobPosting/Broadcast). |
| **Bing Webmaster Tools API** | Bing rank tracking, backlink counts, crawl issues, and query statistics. | `bing-webmaster` MCP | **Active** | `BING_WEBMASTER_API_KEY` | Site URL ➔ Query traffic, crawl stats, links | Bing desktop traffic represents 8–12% market share. |
| **IndexNow Protocol** | Instant multi-engine broadcast (Bing, Yandex, Seznam, Naver) within 60s. | `seo/submit_indexnow.py` | **Active** | `INDEXNOW_KEY`, public key txt file | List of URLs ➔ HTTP 200 broadcast confirmation | Supported by Bing, Yandex; Google does not use IndexNow. |
| **Google Business Profile API** | Local 3-Pack, NAP alignment, verified review response management (Localist). | `vivaak_oauth_flow.py` (`business.manage`) | **Active** | Google Cloud Console OAuth 2.0 | Location ID, reviews ➔ Review responses, local posts | Requires verified business profile and authorized OAuth client. |
| **Firecrawl API** | High-fidelity markdown scraping and structured extraction of competitor sites. | Shadow agent configuration | **Active** | `FIRECRAWL_API_KEY` | Target URLs ➔ Clean Markdown, H1-H3s, tables | Strips bloat; eliminates raw HTML token waste. |
| **Cloudflare D1** | Serverless SQLite relational database at the edge for product/blog storage. | Suntec `scripts/backup_d1_database.py` | **Active** | Cloudflare Wrangler CLI, D1 binding | SQL queries ➔ Tabular relational records | SQLite dialect; transactions limited to single database. |
| **Firebase Realtime Database** | Realtime document storage for inquiries, reservations, and staticDb cache. | Vivaak `vivaak_rtdb_snapshot_latest.json` | **Active** | Firebase Admin SDK, service credentials | JSON trees ➔ Live synchronized application state | Document hierarchy requires structured schema validation. |
| **Local Filesystem JSON** | Zero-dependency canonical data storage conforming to Schema Registry V3.1. | `data/`, `schemas/v3_1/` | **Active** | Standalone Python `validator.py` | Typed JSON files ➔ Immutable historical logs | Standard local store for development and testing. |
| **Next.js 14/15 App Router** | Frontend web application framework hosting SSG pages and metadata. | Target client codebases | **Active** | Node.js, React, Tailwind CSS | React components ➔ Edge-rendered static HTML | Mechanic must run isolated builds before pushing. |
| **Cloudflare Pages & Workers** | Edge hosting and global CDN deployment for pre-rendered static sites. | `deploy-cloudflare.sh`, `wrangler.json` | **Active** | Cloudflare API token, Wrangler | Static build output ➔ Global Edge distribution | Global propagation within seconds; fast edge TTFB. |

---

## 2. MCP Server Configuration

The framework utilizes Model Context Protocol (MCP) servers to grant agents direct, sandboxed tool access to external SEO services.

The authoritative configuration in `~/.gemini/config/mcp_config.json` defines:

```json
{
  "mcpServers": {
    "gsc-mcp": {
      "command": "npx",
      "args": ["-y", "@mikusnuz/gsc-mcp"],
      "env": {
        "GSC_CLIENT_ID": "${GSC_CLIENT_ID}",
        "GSC_CLIENT_SECRET": "${GSC_CLIENT_SECRET}",
        "GSC_REFRESH_TOKEN": "${GSC_REFRESH_TOKEN}"
      }
    },
    "gtm-mcp": {
      "command": "npx",
      "args": ["-y", "google-tag-manager-mcp-server"],
      "env": {
        "GOOGLE_CLIENT_ID": "${GOOGLE_CLIENT_ID}",
        "GOOGLE_CLIENT_SECRET": "${GOOGLE_CLIENT_SECRET}",
        "GOOGLE_REFRESH_TOKEN": "${GOOGLE_REFRESH_TOKEN}"
      }
    },
    "analytics-mcp": {
      "command": "uvx",
      "args": ["analytics-mcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "${GA4_CREDENTIALS_PATH}",
        "GOOGLE_PROJECT_ID": "${GOOGLE_PROJECT_ID}"
      }
    },
    "bing-webmaster": {
      "command": "/Users/viyogianand/.gemini/bin/bwt-mcp-go-darwin-arm64",
      "env": {
        "BING_WEBMASTER_API_KEY": "${BING_WEBMASTER_API_KEY}",
        "BING_INDEXNOW_KEY": "${BING_INDEXNOW_KEY}"
      }
    },
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "dataforseo-mcp-server"],
      "env": {
        "DATAFORSEO_LOGIN": "${DATAFORSEO_LOGIN}",
        "DATAFORSEO_PASSWORD": "${DATAFORSEO_PASSWORD}"
      }
    },
    "hostinger": {
      "command": "npx",
      "args": ["-y", "@hostinger/mcp"],
      "env": {
        "HOSTINGER_API_TOKEN": "${HOSTINGER_API_TOKEN}"
      }
    }
  }
}
```

---

## 3. Tool Mediation Patterns

The system distinguishes between three tool interaction patterns:

1. **Native MCP Server Tools:** Eagerly or lazily loaded tools invoked directly by agents during turn execution (e.g. `gsc-mcp:search_analytics_query`, `dataforseo:api_request`, `analytics-mcp:run_report`).
2. **Deterministic Script Tools:** Executable Python and Node.js command-line utilities managed via `run_command` or background tasks (e.g., `seo/run_phase1_intelligence.py`, `seo/submit_indexnow.py`, `scripts/build_full_tracker.py`).
3. **Pluggable Database Adapters:** Direct Python or Node.js drivers interacting with Cloudflare D1 or Firebase RTDB to query `KNOWLEDGE_FACT` and `STRATEGY_STATE` records.

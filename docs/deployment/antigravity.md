# Google Antigravity Native Deployment Guide
## Complete Setup for Google Antigravity Agentic IDE & Python SDK

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — ANTIGRAVITY DEPLOYMENT GUIDE
========================================================================================
```

## 1. Environment Prerequisites
- macOS (Apple Silicon or Intel) or Linux (Ubuntu 22.04+).
- Google Antigravity Agentic IDE installed.
- Python 3.11+ with standard library and SQLite3.
- Node.js 20+ LTS with `npx` and `uvx` available on `$PATH`.

---

## 2. Directory Layout & Workspace Setup
Clone or place the framework repository inside your active Antigravity workspace:
```bash
cd "/Users/username/Desktop/YourProject"
git clone https://github.com/viyogianand/viyogi-agentic-seo-swarm.git
cd viyogi-agentic-seo-swarm
cp .env.example .env
```

---

## 3. Configuring MCP Servers in Antigravity
Add the required Model Context Protocol (MCP) servers to your global Antigravity configuration file at `~/.gemini/config/mcp_config.json`:

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
    "analytics-mcp": {
      "command": "uvx",
      "args": ["analytics-mcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "${GA4_CREDENTIALS_PATH}",
        "GOOGLE_PROJECT_ID": "${GOOGLE_PROJECT_ID}"
      }
    },
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "dataforseo-mcp-server"],
      "env": {
        "DATAFORSEO_LOGIN": "${DATAFORSEO_LOGIN}",
        "DATAFORSEO_PASSWORD": "${DATAFORSEO_PASSWORD}"
      }
    }
  }
}
```

---

## 4. Subagent Definition in Antigravity
The framework uses native Antigravity subagents. You can invoke them directly in the chat or define specialized execution subagents using `define_subagent`:

```json
{
  "name": "seo_sentinel",
  "description": "Zero-tolerance verification gate for factual claims and JSON-LD schemas.",
  "system_prompt": "You are Sentinel (#19). You audit content drafts against knowledge-bank/ and schemas/v3_1/.",
  "enable_write_tools": false,
  "enable_subagent_tools": false
}
```

---

## 5. First-Run Validation
Run the built-in diagnostic test to verify that the environment, engines, and schemas are operational:
```bash
python3 scripts/test_search_intelligence.py
```
*Expected Output: `Ran 11 tests ... OK`*

# Installation & Deployment Guide
## Setting Up Viyogi Agentic SEO Swarm from Scratch

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — INSTALLATION GUIDE
========================================================================================
```

## 1. Step-by-Step Installation

### Step 1: Clone or Initialize the Repository
```bash
git clone https://github.com/viyogi/viyogi-agentic-seo-swarm.git
cd viyogi-agentic-seo-swarm
```

### Step 2: Configure Environment Variables
Create a local `.env.local` file by copying the example template:
```bash
cp .env.example .env.local
```
Populate `.env.local` with your DataForSEO credentials, Google Client ID/Secret, and Bing API keys (see [Environment Variables Guide](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/setup/environment-variables.md)).

### Step 3: Verify Python & Node Environments
```bash
python3 --version  # Must be >= 3.10
node --version     # Must be >= 18.0
```

### Step 4: Run Canonical Schema Validation
Verify that the canonical schema suite and validator function correctly:
```bash
python3 schemas/v3_1/validator.py
```
Expected output:
```
============================================================
VIVAAK / VAZA CANONICAL SCHEMA VALIDATOR V3.1
============================================================
Loaded 30 schema definitions from schemas/v3_1/
Testing validation logic on sample records...
  ✓ entity.json test record passed
  ✓ page.json test record passed
  ✓ keyword.json test record passed
  ✓ forecast.json test record passed
============================================================
ALL SYSTEM SCHEMAS VERIFIED SUCCESSFULLY!
============================================================
```

### Step 5: Configure MCP Servers
Add the required MCP server definitions to your global Antigravity MCP configuration file at `~/.gemini/config/mcp_config.json` (see [API Integrations Guide](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/setup/api-integrations.md)).

---

## 2. Launching in Google Antigravity IDE

1. Open the repository directory in Google Antigravity IDE.
2. In the Chat / Manager view, initialize the Conductor agent:
   > *"Run initial baseline audit for project [PROJECT_ID]."*
3. Conductor will dispatch Scout and Spyglass to verify connectivity and ingest baseline search performance.

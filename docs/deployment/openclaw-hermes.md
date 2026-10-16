# OpenClaw & Hermes CLI Deployment Guide
## Headless Agent Execution & Containerized Runner Setup

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — OPENCLAW & HERMES DEPLOYMENT GUIDE
========================================================================================
```

## 1. Overview & Capability Boundary

**OpenClaw** and **Hermes** are open-source autonomous agent frameworks running via command-line or containerized daemon runtimes. While they do not provide the graphical pair-programming UI of Google Antigravity, they excel at **unattended background cron execution** (e.g. running Phase 1 daily intelligence scans at 02:00 UTC).

---

## 2. Docker / Containerized Deployment
A standard Dockerfile is provided to containerize the complete Viyogi Python engine suite:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl sqlite3 ca-certificates git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
CMD ["python3", "engines/pilot_cycle.py"]
```

---

## 3. OpenClaw Tool Registration
To register Viyogi engines as tools inside OpenClaw, declare the tool manifest in `openclaw_tools.json`:

```json
{
  "tools": [
    {
      "name": "run_search_intelligence",
      "description": "Executes 10 search intelligence diagnostics for a target keyword.",
      "command": "python3 scripts/search_intelligence_engine.py --query {query} --country {country}",
      "parameters": {
        "query": {"type": "string", "required": true},
        "country": {"type": "string", "default": "US"}
      }
    },
    {
      "name": "submit_indexnow",
      "description": "Broadcasts a newly published URL to the IndexNow protocol.",
      "command": "python3 scripts/submit_indexnow.py {url}",
      "parameters": {
        "url": {"type": "string", "required": true}
      }
    }
  ]
}
```

---

## 4. Hermes CLI Workflow Runner
Hermes executes tasks sequentially by piping intermediate JSON artifacts through the shell:
```bash
# Execute Stage 1 Telemetry Gathering
python3 scripts/run_phase1_intelligence.py --output /tmp/phase1.json

# Pipe findings into the Conductor Decision Engine
python3 engines/pilot_cycle.py --input /tmp/phase1.json
```

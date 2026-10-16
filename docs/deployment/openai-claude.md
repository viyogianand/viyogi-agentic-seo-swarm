# OpenAI Agent SDK & Claude Code Deployment Guide
## Function-Calling Integration & Terminal Harness Setup

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — OPENAI & CLAUDE CODE DEPLOYMENT GUIDE
========================================================================================
```

## 1. Overview & Compatibility

This guide documents how to execute the Viyogi Agentic SEO Swarm using:
1. **OpenAI Agent SDK / Swarm Python Harness:** Using OpenAI models (GPT-4o / o1) via JSON schema function-calling.
2. **Claude Code CLI:** Using Anthropic's interactive command-line agent tool.

---

## 2. OpenAI Function-Calling Adapter
The Viyogi Draft 2020-12 schemas in `schemas/v3_1/` are natively convertible to OpenAI tool definitions:

```python
import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Register Search Intelligence Engine as an OpenAI tool
tools = [
    {
        "type": "function",
        "function": {
            "name": "run_search_intelligence",
            "description": "Runs complete 10-capability search intelligence audit for a commercial keyword.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {"type": "string"},
                    "country": {"type": "string", "default": "US"}
                },
                "required": ["keyword"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Analyze striking-distance and query fan-out for cut wire shot."}],
    tools=tools
)
```

---

## 3. Claude Code CLI Integration
Claude Code operates directly inside terminal directories with bash tool execution:

```bash
# 1. Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 2. Navigate to framework directory
cd /path/to/viyogi-agentic-seo-swarm

# 3. Launch Claude Code with project context
claude
```

Inside the Claude Code prompt, execute workflows directly:
> *"Read `docs/workflows/new-project-onboarding.md` and run the Stage 1 discovery on this repository."*

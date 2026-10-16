# Multi-Runtime Deployment & Adapter Architecture
## Portable Deployment across Google Antigravity, OpenClaw, Hermes, OpenAI Codex & Claude Code

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — RUNTIME DEPLOYMENT SPECIFICATION
========================================================================================
```

## 1. Architectural Portability Principles

The Viyogi Agentic SEO Swarm is engineered to be **runtime-portable**. The core intelligence, schemas, and workflows are completely decoupled from runtime-specific harness code:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PORTABLE CORE SEO FRAMEWORK                          │
│ • Universal Prompts & Agent Specifications (docs/agents/*.md)          │
│ • Canonical Draft 2020-12 JSON Schemas (schemas/v3_1/*.json)          │
│ • Pure Python 3.11+ Engines (engines/*.py, scripts/*.py)               │
│ • Isolated Knowledge Bank (knowledge-bank/*.json)                      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ consumes via runtime adapters
┌───────────────────────────────────▼────────────────────────────────────┐
│                    SUPPORTED AGENT EXECUTION RUNTIMES                  │
├─────────────────┬──────────────────┬─────────────────┬─────────────────┤
│ Google          │ OpenClaw /       │ OpenAI Agent /  │ Claude Code /   │
│ Antigravity     │ Hermes CLI       │ Codex CLI       │ Claude CLI      │
│ (Native Host)   │ (Docker / CLI)   │ (Python Runner) │ (Bash / Tools)  │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘
```

---

## 2. Runtime Compatibility Matrix

| Runtime Environment | Implementation Status | Tool Calling Protocol | Concurrency Model | Persistent Memory | Sandboxing Model |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Google Antigravity** | **Verified Operational** | Native Eager/Lazy MCP (`mcp_config.json`) | Native Subagents (`invoke_subagent`) | 4-Tier SQLite (`strategic_memory.db`) | Workspace branch sandboxing |
| **OpenClaw** | **Designed & Documented** | OpenClaw Tool Specs / CLI Pipes | Worker Thread Pool | SQLite / JSON Filesystem | Containerized Docker volume |
| **Hermes** | **Designed & Documented** | Hermes Skill Tool Manifests | Async Process Scheduler | Local State File (`hermes_state.json`)| Process isolation |
| **OpenAI Agents / Codex**| **Tested (Python Runner)** | Function Calling (JSON Schema) | `asyncio.gather` with Semaphore | SQLite / Redis Key-Value | Virtualenv / Docker sandbox |
| **Claude Code (CLI)** | **Tested (Bash / Tools)** | Standard Bash Tool Execution (`run_command`)| Sequential / Subagent CLI | Local Filesystem JSON | Terminal subshell execution |

---

## 3. Deployment Guides by Runtime

Detailed step-by-step installation, environment configuration, and verification instructions are documented in dedicated runtime manuals:

1. **[Google Antigravity Deployment Guide](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/deployment/antigravity.md)**: Native execution inside Google Antigravity IDE, subagent configuration, and MCP server setup.
2. **[OpenClaw & Hermes Deployment Guide](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/deployment/openclaw-hermes.md)**: CLI and containerized execution for open-source autonomous agent harnesses.
3. **[OpenAI & Claude Code Deployment Guide](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/deployment/openai-claude.md)**: Function-calling integration for OpenAI Agent SDK and Claude Code terminal harnesses.
4. **[Runtime Troubleshooting & Common Pitfalls](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/deployment/troubleshooting.md)**: Resolving Node.js MCP spawn errors, Python path mismatches, and token rate limits.

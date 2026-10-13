# Contributing to Viyogi Agentic SEO Swarm
## Developer Guide for Extending Agents, Schemas, Workflows & Intelligence Engines

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — CONTRIBUTING GUIDELINES
========================================================================================
```

Thank you for your interest in contributing to **Viyogi Agentic SEO Swarm**! This document provides instructions for developers, technical collaborators, and contributors looking to extend the framework safely.

---

## 1. Architectural Rules for Contributors

1. **Decoupled Architecture:** Reusable reasoning logic and tools belong in `docs/` and `scripts/`. Business-specific facts, proprietary specs, and private credentials belong strictly in `knowledge-bank/` and `.env.local`. Never hardcode business facts into agent prompts.
2. **Strict Schema Conformance:** All records passed between agents or written to storage must strictly satisfy the schemas in `schemas/v3_1/`. Run `python3 schemas/v3_1/validator.py` before committing.
3. **No Hallucinated Claims:** Any new agent or workflow modifying content must be routed through **Sentinel (#3)** for verification against the Knowledge Bank.
4. **Token-Efficiency First:** Mechanical calculations (math, diffs, table transformations) must be implemented as Python algorithms (stateless Intelligence Engines), not open-ended LLM prompts.
5. **Human Approval Safeguards:** Never bypass `APPROVAL_QUEUE.md` for production code modifications, CMS updates, or external communication.

---

## 2. How to Add a New Agent

To introduce a new specialized agent to the swarm:

1. **Verify Need:** Confirm that the proposed responsibility requires persistent strategic reasoning and cannot be accomplished by an existing agent or a stateless Intelligence Engine.
2. **Create Agent Documentation:**
   Add `docs/agents/[agent-name].md` using the standard 15-part template:
   - A. Identity, B. Purpose, C. Responsibilities, D. Capabilities, E. Inputs, F. Tools & Integrations, G. Processing Logic, H. Outputs, I. Inter-Agent Communication, J. Memory, K. Autonomy, L. Error Handling, M. Evaluation, N. Limitations, O. Extension Guide.
3. **Register in Agent Index:**
   Add the agent to `docs/agents/README.md` and `docs/architecture/agent-topology.md`.
4. **Define Input/Output Schemas:**
   If the agent emits a new object type, define its JSON Schema in `schemas/v3_1/` conforming to Draft 2020-12.
5. **Assign Model Tier:**
   Assign the agent to an appropriate model tier in `docs/architecture/model-routing.md` (Flash for data parsing; Pro for synthesis/drafting).
6. **Implement Python Runner or Markdown Config:**
   Provide the runner function in Python or custom agent Markdown definition.

---

## 3. How to Connect a New SEO API or MCP Server

1. **Add MCP Server Definition:**
   Document the server configuration in `docs/architecture/tech-stack.md` and add the sandbox config to `~/.gemini/config/mcp_config.json`.
2. **Wrap in Resilient Tool Function:**
   Implement exponential backoff, rate limiting, and an explicit fallback mode (returning `null` and `Evidence State: UNKNOWN` if the service is unavailable).
3. **Add Environment Variables:**
   Add the required API keys to `.env.example` and document them in `docs/setup/environment-variables.md`.

---

## 4. How to Test Changes

Before submitting a Pull Request:
```bash
# 1. Validate all schemas
python3 schemas/v3_1/validator.py

# 2. Test intelligence crawler
python3 scripts/run_phase1_intelligence.py

# 3. Test frontend build (if modifying Next.js codebase)
npm run build
```

---

## 5. Pull Request & Commit Guidelines

- Use conventional commits:
  - `feat(agents): add local grid ranking capability to Localist`
  - `fix(schemas): enforce ISO 8601 regex on date fields`
  - `docs(workflows): add multi-language translation pipeline`
- Ensure all tests pass and documentation is updated in sync with code.

# Model Routing & Token Optimization
## Tiered Model Allocation, Cost Management & Token Guardrails

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — MODEL ROUTING & OPTIMIZATION SPECIFICATION
========================================================================================
```

## 1. Core Routing Principle

> **"Spend tokens where the objective is won (Strategy, Drafting, Verification); economize everywhere the task is merely data organization."**

In traditional agent swarms, assigning expensive reasoning models to every agent results in unsustainable API bills and severe rate limits. Conversely, assigning weak models to drafting or verification causes generic AI clichés and catastrophic factual hallucinations.

The Viyogi framework resolves this through **Tiered Model Routing**:
- **Reasoning Spend tracks Decision Stakes and Error Cost**, not agent seniority.
- **Stateless Intelligence Engines** handle mathematical calculations and data diffing with **zero LLM cost**.

---

## 2. Master Agent Model Routing Matrix

| Tier | Target LLM Models | Assigned Agents | Workload Character | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Heavyweight / Pro Tier** | • Gemini 3.1 Pro<br>• Claude 3.7 Sonnet | • **Conductor** (#1)<br>• **Editor** (#20)<br>• **Forecaster** (#21)<br>• **Scribe** (#12)<br>• **Sentinel** (#3)<br>• **Mechanic** (#16) | Complex synthesis, multi-variable strategic planning, authoritative human-grade writing, zero-tolerance verification, production code modification. | High error cost. A hallucinated specification or poor editorial plan invalidates the entire downstream workflow. Scribe and Sentinel are the non-negotiable quality anchors. |
| **Mid Tier** | • Gemini 3.0 Flash<br>• Claude 3.5 Haiku | • **Answerer** (#14)<br>• **Networker** (#18)<br>• **Herald** (#19)<br>• **Scholar** (#17) | Precise semantic extraction, natural human outreach drafting, policy validation. | Needs natural, non-robotic phrasing for PR pitches and direct-answer snippets without requiring deep multi-step planning. |
| **Lightweight / Fast Tier** | • Gemini 3.0 Flash-Lite<br>• GPT-4o-mini | • **Archivist** (#2)<br>• **Scout** (#4)<br>• **Prospector** (#5)<br>• **Shadow** (#6)<br>• **Envoy** (#7)<br>• **Gardener** (#8)<br>• **Beacon** (#9)<br>• **Reporter** (#10)<br>• **Spyglass** (#11)<br>• **Tuner** (#13)<br>• **Schema Master** (#15)<br>• **Localist** ([+])<br>• **Courier** ([+]) | Parsing structured API JSON, regex checks, metadata length verification, JSON-LD generation, API broadcasting. | Near-zero reasoning difficulty. The intelligence was already computed by the API (DataForSEO, GSC) — these agents organize, parse, and reformat data. |

---

## 3. The 6 Token-Optimization Protocols

### Protocol 1: Zero Raw HTML in Reasoning Contexts
Never feed raw scraped HTML or 2MB web payloads into model context windows.
- Web scrapers (Firecrawl, Python `RobustHTMLParser`) must extract **only** headings (H1–H3), word count, schema blocks, and clean body text.
- Eliminates 80–90% of token consumption per scraped competitor page.

### Protocol 2: Archivist is a Cache, Not a Re-Derivation
Agents must never re-read raw PDFs, re-summarize the Knowledge Bank, or re-verify specs during routine turns.
- Archivist provides pre-indexed, verified `KNOWLEDGE_FACT` records via quick vector/database lookups.
- Avoids spinning up massive repetitive context windows across 22 agents.

### Protocol 3: Claim-Level Verification Over Document Re-Analysis
Sentinel does not re-read entire 3,000-word articles end-to-end to check facts:
- Tuner or a fast extraction script extracts a discrete list of factual claims (`[ "Density: 7.8 g/cm³", "Capacity: 6 BHK" ]`).
- Sentinel verifies only this discrete structured list against Archivist's facts.
- Reduces verification token expenditure by up to 75% per draft.

### Protocol 4: Batched Requests Over Iterative Loops
Never invoke an agent 50 times in a loop to evaluate 50 keywords.
- Scout fetches 50 keywords in a single batched DataForSEO call.
- Prospector clusters all 50 keywords in a single structured prompt pass.

### Protocol 5: Scheduled Execution Prevents Idle Token Waste
Agents do not run continuously in an unconstrained polling loop:
- **Pool A (Intelligence):** Runs on a weekly/monthly cron schedule.
- **Pool B (Assembly Line):** Runs strictly on demand when Conductor prioritizes an approved Content Brief.
- **Idle Cost:** Exactly \$0.00 between scheduled runs.

### Protocol 6: Internal Structured JSON Over Conversational Prose
Intermediate agent handoffs (Scribe ➔ Tuner ➔ Answerer ➔ Schema Master) pass compact, typed JSON objects conforming to the V3.1 Canonical Data Contract.
- Eliminates the need for downstream agents to parse ambiguous conversational prose.
- Preserves context window fidelity across long assembly lines.

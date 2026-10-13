# Agent Specification: Conductor (#1)
## Chief Growth Director & Strategic Brain

```
========================================================================================
AGENT SPECIFICATION — CONDUCTOR
========================================================================================
```

### A. Identity
- **Agent Name:** Conductor
- **Agent ID:** `agent_conductor`
- **Functional Category:** Layer 1: Governance & Strategic Brain
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises (V1 & V2) & VivaakVaza (V3)
- **Relevant Implementation Files:**
  - `docs/architecture/architecture-overview.md`
  - `orchestrator.py` / Antigravity Conductor Prompt
  - `SUNTEC_AGENTIC_SEO_AGENT_ROSTER_V2.md`
  - `VIVAAK_AGENTIC_SEO_AGENT_ROSTER_V3.md`

---

### B. Purpose
Conductor exists to solve the fundamental question: **"What is the highest-value next action for this business based on empirical data, commercial revenue potential, and explicit uncertainty?"** It eliminates aimless task execution by anchoring the entire swarm to commercial North Star metrics.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Evaluating macro telemetry from GSC, GA4, DataForSEO, and the Opportunity Engine.
  - Answering the **12 Strategic Questions** at the start of every operational cycle.
  - Determining the **Next Best Action** (`NEXT_BEST_ACTION`).
  - Dispatching tasks to Pool A, Editor, Forecaster, and Pool B.
  - Managing resource allocation and execution scheduling.
- **Out of Scope (Does Not Own):**
  - Drafting content (owned by Scribe).
  - Verifying factual claims (owned by Sentinel).
  - Directly modifying codebase or production databases (owned by Mechanic).

---

### D. Capabilities
- **Verified Capabilities:**
  - Dynamic task scheduling and queue prioritization based on commercial scores.
  - Strategic memory synthesis (querying Archivist before generating new action plans).
  - Direct coordination of subagents via `invoke_subagent`.
- **Partially Implemented:**
  - Multi-variable trade-off optimization between content updates vs new creation (partially delegated to Editor).
- **Planned Capabilities:**
  - Automated dynamic budget rebalancing between API pools based on marginal attribution return.

---

### E. Inputs
- **Required Context:**
  - Latest `STRATEGY_STATE` from Archivist.
  - Top 10 `CONTENT_OPPORTUNITY` records from the Opportunity Engine.
  - 28-day performance deltas from GSC and GA4.
- **Trigger Conditions:**
  - Scheduled weekly growth cycle.
  - Alert from Spyglass regarding sudden indexing drops or traffic anomalies.
- **Upstream Dependencies:** Archivist, Spyglass, Opportunity Engine.

---

### F. Tools and Integrations
- `invoke_subagent`: Dispatches tasks to Pool A, Editor, Forecaster, Mechanic.
- `StorageAdapter.query`: Queries Strategic Memory and previous experiment outcomes.
- Task Queue Manager: Reads and writes the central action queue.

---

### G. Processing Logic
In every operational cycle, Conductor answers the **12 Strategic Questions**:
1. What changed in search and business telemetry?
2. Why did it change?
3. What matters commercially (RFQs, bookings, revenue)?
4. What striking-distance or gap opportunities exist?
5. Which opportunity has the highest composite score?
6. What empirical evidence supports pursuing it?
7. What is the expected outcome?
8. What is the range forecast (P10/P50/P90)?
9. Should we Create, Update, Consolidate, or Do Nothing?
10. What specific agent action queue is required?
11. How will success be measured over 28 days?
12. When is the review milestone?

---

### H. Outputs
- **Format:** Structured JSON conforming to `NEXT_BEST_ACTION` and `STRATEGY_STATE`.
- **Schema:** `schemas/v3_1/next_best_action.json`
- **Example Output:**
```json
{
  "action_id": "act_20261013_vaza_pool",
  "date": "2026-10-13",
  "action": "Update Vaza Villa page title, H1, and FAQ to target 'luxury villa with heated pool'",
  "page_id": "page_vaza_villa",
  "keyword_id": "kw_luxury_villa_heated_pool",
  "opportunity_id": "opp_vaza_heated_pool",
  "reason": "Striking distance rank (pos 8.4) with zero competitors offering private heated pool proof.",
  "evidence": "GSC 120 impressions/wk with 1.2% CTR; DataForSEO shows snippet takeover opportunity.",
  "expected_impact": "HIGH",
  "effort": "LOW",
  "confidence": "HIGH",
  "dependencies": ["fact_vaza_heated_pool_temperature"],
  "owner": "Editor",
  "approval_required": "LEVEL_B",
  "deadline": "2026-10-15T18:00:00Z",
  "status": "APPROVED"
}
```
- **Downstream Consumers:** Editor, Forecaster, Pool B Assembly Line.

---

### I. Inter-Agent Communication
- **Calls:** Archivist (reads memory), Scout/Prospector/Shadow (gathers intelligence), Editor (delegates briefing), Forecaster (requests range model).
- **Called By:** Human Growth Director via Antigravity Manager View or Scheduled Tasks cron.

---

### J. Memory and Persistence
- **Reads:** `STRATEGY_STATE`, `LEARNING`, `STRATEGIC_RULE`, `KNOWLEDGE_FACT`.
- **Writes:** Updates `STRATEGY_STATE` at the conclusion of each weekly strategic cycle.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A for analysis, task dispatch, and memory reading.
- **Escalation Trigger:** Requires human approval if proposing to retire a high-traffic URL or modify core brand positioning.

---

### L. Error Handling
- **Missing Telemetry:** Falls back to cached 7-day GSC/GA4 records from Archivist with explicit `confidence: LOW`.
- **Conflicting Signals:** Emits a `STRATEGY_HOLD` alert and routes the decision to human review rather than guessing.

---

### M. Evaluation
- Evaluated on whether the dispatched actions yield positive movement on North Star metrics across the 28-day window.

---

### N. Limitations
- Dependent on first-party telemetry accuracy; cannot independently diagnose tracking outages without Spyglass.

---

### O. Extension Guide
To extend Conductor for a new industry vertical, register new commercial intent weighting algorithms in the Opportunity Engine; Conductor's core 12-question decision logic remains unchanged.

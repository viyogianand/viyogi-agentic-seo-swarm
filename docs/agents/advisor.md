# Agent Specification: Advisor (Legacy V1)
## Task-List Bookkeeper & Project Tracker

```
========================================================================================
AGENT SPECIFICATION — ADVISOR (LEGACY / CONSOLIDATED SUB-ROLE)
========================================================================================
```

### A. Identity
- **Agent Name:** Advisor
- **Agent ID:** `agent_advisor`
- **Functional Category:** Governance & Project Tracking (Legacy Sub-Role)
- **Implementation Status:** Consolidated into Conductor in V2.0 / V3.0
- **Source Project:** Suntec Enterprises V1.0 (`Suntec Agentic SEO Swarm — Antigravity IDE Implementation (Token-Optimized).md`)
- **Relevant Implementation Files:**
  - `Downloads/Suntec Agentic SEO Swarm — Antigravity IDE Implementation (Token-Optimized).md`
  - `docs/architecture/architecture-reconciliation.md`

---

### B. Purpose
In the original System V1.0 architecture (September 2026), Advisor functioned as the lightweight task-list bookkeeper. Its mission was to maintain checklist statuses, audit due dates, and track task progression across manual spreadsheets without consuming heavy model tokens.

---

### C. Evolution & Consolidation Status
In **System V2.0 and V3.0**, the static checklist spreadsheet was replaced by:
1. **Conductor's Dynamic Task Queue:** Manages operational task prioritization using real-time Opportunity Scores.
2. **Reporter's Automated Python Dashboards:** Compiles Excel and Markdown progress trackers autonomously.
3. **The 18-Step Closed-Loop Decision Engine:** Formalizes task progression from observation through measurement.

Consequently, Advisor's standalone agent duties were absorbed directly into Conductor and the Opportunity Engine.

---

### D. Capabilities (V1 Baseline)
- **Verified Capabilities:**
  - Tracking status columns (`TODO`, `IN_PROGRESS`, `DONE`, `BLOCKED`) in Markdown tables.
  - Due date verification and milestone reminders.
- **Current Operational Role:**
  - Documented as an optional lightweight subagent (`model: flash-lite`) for standalone CLI deployments lacking a central database task manager.

---

### E. Inputs & Outputs
- **Input:** Task list items and completion timestamps.
- **Output:** Updated task backlog Markdown tables.

---

### F. Extension Guide
If deploying the swarm in an environment without an automated task engine (such as a pure Markdown repository), Advisor can be reactivated as a lightweight task clerk. In standard Viyogi framework deployments, all task scheduling is managed dynamically by Conductor.

# Learning Review & Policy Promotion Protocol
## Governance, Risk Assessment & Automated Rollback Procedures for System Learnings

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — LEARNING REVIEW SPECIFICATION
========================================================================================
```

## 1. Objective & Scope

This specification defines the formal review, evaluation, risk assessment, and approval process before any empirical learning recorded in `learning-log.md` is promoted into a binding Level 4 Strategic Rule or committed as a core framework modification.

---

## 2. Review Cadence & Authority

1. **Bi-Weekly Review Cadence:** Conductor (#1) and Editor (#20) aggregate newly recorded observations every 14 days.
2. **Promotion Gate Authority:**
   - **Internal Heuristics (Level 3):** Can be promoted autonomously by Archivist if supported by $\ge 3$ consistent experimental observations with $\text{PES} \le 0.3$.
   - **Binding Strategic Rules (Level 4):** Requires explicit human approval via `APPROVAL_QUEUE.md`.
   - **Core Prompt or Code Changes:** Requires a formal Change Proposal and regression test execution.

---

## 3. Four-Dimensional Risk & Value Scoring Model

Before proposing a change to the core framework, the learning is scored across four objective criteria (1–5 scale):

$$\text{Promotion Priority Score} = \frac{\text{Value} \times \text{Confidence}}{\text{Risk} \times \text{Effort}}$$

| Dimension | 1 (Low) | 3 (Moderate) | 5 (High) |
| :--- | :--- | :--- | :--- |
| **Value (Impact)** | Minor syntax or formatting tweak. | Improved on-page CTR or SERP rank gain. | Unlocks major commercial conversions or recovers site penalty. |
| **Confidence** | Observed once in a single query. | Measured consistently across 1 client over 30 days. | Verified across $\ge 2$ independent client verticals. |
| **Risk** | Read-only reporting or telemetry logging. | Content update to existing secondary pages. | Core robots.txt, 301 redirects, or site-wide canonical changes. |
| **Effort** | Single configuration parameter update. | Script modification or schema extension. | Multi-agent architectural refactoring. |

---

## 4. Change Proposal Template

When a learning qualifies for core implementation, the following ticket is submitted to `APPROVAL_QUEUE.md`:

```markdown
### [CHANGE PROPOSAL] Promotion of Learning LRN-20261016-001 to RULE_004
- **Originating Learning ID:** `LRN-20261016-001`
- **Target Policy:** Level 4 Strategic Rule `RULE_004: BRAND_ENTITY_HOMEPAGE_STRUCTURE`
- **Proposed Rule Definition:**
  > "For any brand with historical presence on third-party B2B directories, the official homepage MUST contain the exact legal entity name in the primary H1 tag, configure Organization schema with sameAs linking to directory profiles, and include an outbound entity reclamation link."
- **Affected Agents:** Conductor, Editor, Tuner, Schema Master, Sentinel
- **Regression Test Command:** `python3 -m unittest tests/test_brand_serp_rules.py`
- **Rollback Procedure:** Remove RULE_004 from `data/strategic_memory.db` and revert `docs/reference/seo-quality-gates.md`.
```

---

## 5. Automated Rollback Protocol

If a newly deployed learning or strategic rule causes an unexpected performance regression (e.g. >15% drop in organic impressions or a rise in crawl errors within 14 days):
1. **Automated Alert:** Spyglass detects the anomaly and flags `REGRESSION_ALERT` to Conductor.
2. **Immediate Reversion:** The Git commit implementing the change is reverted in an isolated branch.
3. **Quarantine State:** The learning entry in `data/strategic_memory.db` is marked `QUARANTINED` and blocked from influencing future agent prompts until re-evaluated.

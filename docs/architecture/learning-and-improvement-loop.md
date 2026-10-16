# Cross-Cutting Learning & Continuous Improvement Loop
## Automated Epistemic Learning, Rule Promotion & Retrospective Forecast Calibration

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — LEARNING & IMPROVEMENT SPECIFICATION
========================================================================================
```

## 1. Architectural Mandate: Anti-Amnesia Engine

A critical vulnerability in traditional agentic architectures is the **amnesiac execution loop**:
- Agents repeat failed experiments because historical outcomes are lost between turns.
- Newly discovered tool capabilities or prompt corrections are forgotten after a session ends.
- Model hallucinations are accepted as facts because decisions are ungrounded.

The Viyogi framework resolves this by establishing a **Cross-Cutting Learning and Improvement Loop** operating across all system layers. It continuously ingests execution evidence, evaluates performance against predictions, and promotes empirically confirmed takeaways into permanent policy.

---

## 2. The 11-Stage Learning Lifecycle

Every observation and learning processed by the swarm flows through a formal 11-stage pipeline:

```
[OBSERVE] ➔ [CAPTURE] ➔ [CLASSIFY] ➔ [VERIFY] ➔ [EVALUATE] ➔ [PROPOSE]
    │                                                              │
    ▼                                                              ▼
[MONITOR] ◄─ [VERSION] ◄── [TEST] ◄─── [IMPLEMENT] ◄─── [APPROVE]
```

### Stage Definitions:
1. **OBSERVE:** The system detects an outcome divergence (e.g. ranking movement, crawl error, prompt failure, or AI citation shift).
2. **CAPTURE:** The event is logged into `data/strategic_memory.db` with an immutable provenance UUID, timestamp, and source metadata.
3. **CLASSIFY:** The learning is categorized:
   - `CLIENT_FACT`: Specific only to the active client (e.g., minimum order quantity, phone number).
   - `REUSABLE_OPERATIONAL`: Applies across all clients (e.g., "OAI-SearchBot requires explicit User-agent allowance").
   - `PROMPT_IMPROVEMENT`: Optimization to agent instructions or few-shot examples.
   - `ARCHITECTURE_CHANGE`: Modification to tools, schemas, or engine pipelines.
   - `HYPOTHESIS`: Unconfirmed empirical trend requiring further testing.
4. **VERIFY:** The observation is cross-referenced against ground truth. For factual claims, Archivist checks the Knowledge Bank. For search metrics, DataForSEO or GSC is consulted.
5. **EVALUATE:** The system estimates usefulness, confidence score (0.0–1.0), implementation risk, and token cost.
6. **PROPOSE:** If the learning warrants a change to core behavior or production assets, a formal change ticket is created.
7. **APPROVE:** Consequential changes (code deployments, robots.txt edits, permanent rule additions) are routed to `APPROVAL_QUEUE.md` for human authorization.
8. **IMPLEMENT:** Upon approval, the change is applied to the codebase or knowledge bank in an isolated branch.
9. **TEST:** Regression test suites (`tests/`) are executed to verify that the change causes no unintended regressions.
10. **VERSION:** The learning is assigned an incremented version ID and committed to Git with an explanatory changelog entry.
11. **MONITOR:** Post-release telemetry is tracked across 28 days to confirm that the change produced the expected benefit.

---

## 3. Four-Tier Memory Promotion Dynamics

The heart of the learning system is the **Bayesian Promotion Engine** implemented in `engines/strategic_memory.py`:

```
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL 4: STRATEGIC RULES (Codified System Policy)                      │
│ • Permanent behavioral rules binding on all agents.                    │
│ • Example: RULE_003: "AEO direct answer blocks must contain exactly    │
│   40–60 words and begin with an entity reference."                     │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ Promoted after validation across >= 3 clients
┌───────────────────────────────────┴────────────────────────────────────┐
│ LEVEL 3: CAUSAL LEARNINGS (Attributed Empirical Takeaways)             │
│ • Verified relationship between an action and a measured outcome.      │
│ • Example: "Adding comparative Ervin fatigue cycles increased AI       │
│   Overview presence by 14% across procurement queries."                │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ Derived from measured telemetry
┌───────────────────────────────────┴────────────────────────────────────┐
│ LEVEL 2: EMPIRICAL OBSERVATIONS (Time-Series Evidence Stream)         │
│ • Raw measurement records captured by Scout, Shadow, and Spyglass.     │
│ • Example: "Competitor Winoa modified H2 tags on /cut-wire-shot;       │
│   gained position 2 for 'cut wire shot supplier'."                     │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ Grounded against
┌───────────────────────────────────┴────────────────────────────────────┐
│ LEVEL 1: GROUNDED BUSINESS FACTS (Immutable Single Source of Truth)    │
│ • Verified corporate facts, physical product specs, and legal claims.  │
│ • Maintained in knowledge-bank/*.json. Zero model inference permitted. │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Retrospective Forecast Calibration (Prediction Error Score)

To prevent agents from generating overly optimistic traffic and ranking projections, **Forecaster (#21)** executes retrospective calibration:

### The Prediction Error Score (PES) Formula:
$$\text{PES} = \left| \frac{\text{Actual Metric Value} - \text{P50 Predicted Target}}{\text{Baseline Metric Value} - \text{P50 Predicted Target}} \right|$$

- **PES = 0.0:** Perfect prediction (actual equals P50).
- **0.0 < PES $\le$ 0.3:** Exceptional calibration (well within confidence interval).
- **0.3 < PES $\le$ 0.7:** Moderate drift (acceptable for volatile SERP environments).
- **PES > 1.0:** Forecast failure (actual moved opposite to prediction or failed completely).

When a completed 28-day experiment produces a $\text{PES} > 0.7$, Forecaster triggers a **Model Calibration Cycle**, reducing future confidence bounds and recording the causal divergence into `backlink_learnings` and `experiments_registry`.

---

## 5. Change Control & Safety Boundaries

To prevent self-reinforcing bias or unauthorized modifications:
1. **Zero Autonomous Core Overwrites:** Agents may never modify their own system prompts, core orchestration logic, or security policies without human approval.
2. **Client Sandboxing Guarantee:** Learnings derived from Client A (e.g. Suntec metallurgy) are cryptographically forbidden from contaminating Client B's Knowledge Bank (e.g. Vivaak hospitality).
3. **Rollback Mechanism:** Every approved learning that modifies a configuration or script includes an automated rollback plan stored in `docs/operations/learning-review.md`.

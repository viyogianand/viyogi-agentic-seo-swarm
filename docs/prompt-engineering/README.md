# Prompt Engineering Playbook & Master Library
## Standard Operating Procedures for Prompt Construction, Model Context & Agent Directives

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — PROMPT ENGINEERING PLAYBOOK
========================================================================================
```

## 1. Core Principles of Autonomous SEO Prompt Engineering

To guarantee predictable, hallucination-free execution across heterogeneous LLM runtimes (Gemini 2.5 Pro/Flash, Claude 3.5 Sonnet, GPT-4o), every prompt in the Viyogi framework adheres to **Six Core Principles**:

1. **Epistemic Classification Standard (Rule Zero Speculation):**
   - Every metric, observation, and assertion must be explicitly tagged as `[OBSERVED]`, `[INFERRED]`, or `[UNAVAILABLE]`.
   - Never allow models to invent search volumes, rankings, or business statistics.
2. **Inspect Before Act:**
   - Prompts mandate that agents inspect existing codebase files, schemas, and `strategic_memory.db` before drafting or deciding.
3. **Structured Machine-Readable Output Contracts:**
   - Outputs must conform to the V3.1 JSON Schemas (Draft 2020-12) or standardized Markdown tables.
4. **Separation of Cognitive Roles (No Monolithic Prompts):**
   - Separate research (Pool A) from editorial strategy (Editor), drafting (Scribe), on-page tuning (Tuner), and verification (Sentinel).
5. **Human Approval Boundaries (Level A vs B vs C):**
   - Read-only diagnostics execute autonomously (Level A). Production code edits, 301 redirects, and outreach require human confirmation (Level B/C).
6. **Graceful Degradation:**
   - Prompts include explicit instructions on fallback mechanisms when specific APIs (e.g. GSC) are unauthenticated.

---

## 2. Standard Prompt Architecture Template

Every production prompt entry in the Viyogi library follows this 12-part structure:

```markdown
### Prompt ID: [STAGE-OBJ-001]
- **Title:** [Human-readable name]
- **Target Agent & Model Tier:** [e.g. Conductor (#1) | Pro Tier]
- **Lifecycle Stage:** [e.g. Stage B: Baseline Intelligence]
- **When to Use:** [Explicit trigger condition]
- **When NOT to Use:** [Inappropriate use cases]
- **Required Context & Inputs:** [Files, data schemas, API credentials needed]
- **Preconditions:** [System state required before execution]
- **Copy-Ready Prompt Text:** [Exact text to execute or pass to runtime]
- **Expected Deliverables / Output Schema:** [JSON schema or Markdown structure]
- **Validation Checklist:** [Verification rules]
- **Common Failure Modes & Fixes:** [Troubleshooting instructions]
- **Approval Gate:** [Level A, B, or C]
```

---

## 3. Master Prompt Library Index by Lifecycle Stage

| Prompt ID | Prompt Title | Target Agent | Model Tier | Lifecycle Stage | Primary Objective |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`ONB-001`** | **Autonomous Project Onboarding** | Conductor (#1) | Pro | Stage A: Onboarding | Inspect workspace, audit tools, and generate initial Project Execution Plan. |
| **`INT-001`** | **Tool & Integration Pre-Flight Audit** | Spyglass (#22) | Flash-Lite | Stage A: Discovery | Validate DataForSEO, GSC, GA4, Bing, and IndexNow API connectivity. |
| **`BND-001`** | **Brand SERP Recovery Diagnostic** | Scout (#4) | Flash-Lite | Stage B: Baseline | Diagnose brand entity splitting, competing domains, and canonical drift. |
| **`GEO-001`** | **30-Day AI Visibility & Citation Sprint** | Beacon (#9) | Flash | Stage B / G: AEO/GEO | Curate 24-query AI panel, measure AI Overview presence, and track SOV. |
| **`MAG-001`** | **Linkable Asset & Benchmark Magnet** | Scribe (#10) / Envoy (#6) | Pro | Stage F: Authority | Architect original technical benchmark tables and statistics hubs. |
| **`EDT-001`** | **Strategic Create vs Update Decision** | Editor (#20) | Pro | Stage E: Content Strategy | Evaluate query opportunities; output formal `CONTENT_BRIEF` records. |
| **`SCB-001`** | **Human-Standard B2B Narrative Drafting**| Scribe (#10) | Pro | Stage E: Content Assembly | Draft deep, expert technical copy strictly obeying Human Writing Guide. |
| **`TUN-001`** | **On-Page Title & Snippet Optimization** | Tuner (#11) | Flash | Stage E: On-Page Tuning | Polish title (<55 chars) and meta description (<155 chars) with CTR hooks. |
| **`ANS-001`** | **Passage Answerability Structuring** | Answerer (#12) | Flash | Stage E: AEO Formatting | Inject 40–60 word direct-answer blocks and PAA accordion answers. |
| **`SCH-001`** | **JSON-LD Entity Graph Construction** | Schema Master (#23)| Flash | Stage E: Technical Ops | Build nested `@graph` schemas linking Organization, Product, and FAQs. |
| **`SNT-001`** | **Zero-Tolerance Claim Verification Gate**| Sentinel (#19) | Pro | Stage E: Verification Gate| Claim-by-claim fact verification; exercises absolute veto on hallucinations. |
| **`MEC-001`** | **Isolated Git Build & Edge Deployment**| Mechanic (#13) | Flash | Stage C: Technical Ops | Run SSG build verification in isolated branch and deploy to Cloudflare. |

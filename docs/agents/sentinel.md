# Agent Specification: Sentinel (#3)
## Zero-Tolerance Verification Gate & Anti-Hallucination Auditor

```
========================================================================================
AGENT SPECIFICATION — SENTINEL
========================================================================================
```

### A. Identity
- **Agent Name:** Sentinel
- **Agent ID:** `agent_sentinel`
- **Functional Category:** Layer 1: Governance & Strategic Brain
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `docs/architecture/architecture-overview.md`
  - `schemas/v3_1/content_change.json`
  - `schemas/v3_1/validator.py`

---

### B. Purpose
Sentinel exists as the **uncompromising verification gatekeeper**. It audits every drafted article, title tag, specification claim, and schema block before any content can reach human review or production. It possesses absolute veto power over hallucinations, unverified technical claims, and marketing fluff.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Extracting discrete factual claims from content drafts.
  - Verifying every claim against Archivist's verified facts.
  - Auditing JSON-LD schemas against Google Rich Results standards.
  - Enforcing compliance with the project's Human Writing Guide (banned buzzwords).
  - Issuing binding verdicts (`VERIFIED`, `REJECTED`, `REVISION_REQUIRED`).
- **Out of Scope (Does Not Own):**
  - Drafting initial copy (owned by Scribe).
  - Approving deployments (owned by Human Growth Director).
  - Editing production code (owned by Mechanic).

---

### D. Capabilities
- **Verified Capabilities:**
  - **Site Reputation Abuse Monitoring (`ReputationAbuseMonitor`):** Audits application route trees and middleware for unauthorized parasitic subdirectories, scans external outbound links for link rot, spam patterns, or missing security rel tags, and monitors referring domains for high-velocity spam backlink spikes triggering Google's Site Reputation Abuse policies (`scripts/search_intelligence_engine.py`).
  - Claim-by-claim verification diffing.
  - Schema syntax and required property validation.
  - Zero-tolerance veto: instantly blocking deployment when fabricated claims are detected.
- **Partially Implemented:**
  - Automated regex scanning for newly emerging AI travel/marketing buzzwords.
- **Planned Capabilities:**
  - Multi-lingual metallurgical standard cross-verification (DIN vs AMS vs ISO).

---

### E. Inputs
- **Required Context:**
  - Draft text and metadata from Pool B (Scribe, Tuner, Answerer, Schema Master).
  - `KNOWLEDGE_FACT` records from Archivist.
  - Project `human-writing-guide.md` (list of banned buzzwords).
- **Trigger Conditions:** Pool B assembly line completion.
- **Upstream Dependencies:** Schema Master, Archivist.

---

### F. Tools and Integrations
- `ArchivistQuery`: Cross-checks extracted claims against verified records.
- `SchemaValidator`: Validates JSON-LD structures via Draft 2020-12 rules.
- Diff Generator: Produces claim-by-claim audit trails.

---

### G. Processing Logic
1. Extract discrete factual claims from draft:
   - Numerical values, tolerances, dimensions, capacity, pricing, certifications.
2. For each extracted claim:
   - Query Archivist.
   - If fact is absent or differs from verified record, mark claim as `FAIL`.
3. Check text against Banned Buzzwords list:
   - If words like "revolutionizing", "state-of-the-art", "nestled in the lap of nature" appear, mark as `REVISION_REQUIRED`.
4. Validate JSON-LD script blocks:
   - Check `@type`, `@id`, required properties, image URLs.
5. If zero failures: issue `VERIFIED` and route to `APPROVAL_QUEUE.md`.
6. If any failure: issue `REJECTED`, halt pipeline, and emit exact diff to Scribe.

---

### H. Outputs
- **Format:** Structured Verification Verdict.
- **Example Output:**
```json
{
  "verdict_id": "vrd_20261013_001",
  "status": "VERIFIED",
  "claims_audited": 14,
  "claims_passed": 14,
  "claims_failed": 0,
  "schema_status": "VALID",
  "writing_guide_violations": [],
  "timestamp": "2026-10-13T10:30:00Z",
  "next_step": "QUEUE_FOR_HUMAN_APPROVAL"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Schema Master (terminal step of Pool B assembly line).
- **Calls:** Archivist (fact retrieval).
- **Reports To:** `APPROVAL_QUEUE.md` (Human Review) on pass; Scribe on rejection.

---

### J. Memory and Persistence
- **Reads:** `KNOWLEDGE_FACT`, `human-writing-guide.md`.
- **Writes:** Rejection logs to Strategic Memory (observations of failed drafting patterns).

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A autonomous verification and veto authority.
- **Veto Authority:** Absolute. No agent (including Conductor) can override a Sentinel rejection.

---

### L. Error Handling
- **Ambiguous Claim:** Defaults to `REVISION_REQUIRED` with request for explicit citation.
- **Unreachable Archivist:** Fails safe (`REJECTED`) — never assumes facts in the absence of evidence.

---

### M. Evaluation
- Tested via deliberate injection of false claims (e.g. fake hardness numbers or hallucinated amenities) to ensure 100% rejection catch rate.

---

### N. Limitations
- Operates on text and schema data; cannot physically verify if a swimming pool is heated without lab/property confirmation.

---

### O. Extension Guide
To add compliance rules (e.g., medical claims, financial disclosures), add constraint objects to `knowledge-bank/negative-constraints.json`.

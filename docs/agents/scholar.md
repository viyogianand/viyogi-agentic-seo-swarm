# Agent Specification: Scholar (#17)
## Search Engine Policy & Fact Validator

```
========================================================================================
AGENT SPECIFICATION — SCHOLAR
========================================================================================
```

### A. Identity
- **Agent Name:** Scholar
- **Agent ID:** `agent_scholar`
- **Functional Category:** Layer 5: Infrastructure & Operations
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `docs/architecture/tech-stack.md`
  - `knowledge-bank/negative-constraints.json`

---

### B. Purpose
Scholar guards against algorithmic search penalties. It cross-references drafts and recommendations against **Google Search Essentials**, **Helpful Content Guidelines**, **Bing Webmaster Guidelines**, and official industry regulations, ensuring the swarm never employs black-hat tactics, doorway page schemes, or unverified regulatory claims.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Auditing content against Google's spam and manipulation policies.
  - Verifying compliance with EEAT (Experience, Expertise, Authoritativeness, Trustworthiness).
  - Checking drafts for doorway page signals, keyword stuffing, and thin affiliate patterns.
  - Cross-checking official regulatory claims (e.g. ISO/DIN metallurgy guidelines; FSSAI hospitality rules).
- **Out of Scope (Does Not Own):**
  - Claim-by-claim business fact checking (owned by Sentinel).
  - On-page title/meta optimization (owned by Tuner).

---

### D. Capabilities
- **Verified Capabilities:**
  - Compliance evaluation against Google Search Essentials documentation.
  - Identification of doorway page risks (e.g. mass-generating identical geo-targeted pages).
  - Flagging ungrounded algorithm speculation (e.g. caught fabricated "AI disclosure rule" claims).
- **Partially Implemented:**
  - Automated EEAT entity author markup auditing.
- **Planned Capabilities:**
  - Continuous monitoring of Google Search Central policy updates and blog announcements.

---

### E. Inputs
- **Required Context:** Candidate content drafts; target search intent; structural URL hierarchy.
- **Trigger Conditions:** Assembly line review; new programmatic template proposals.
- **Upstream Dependencies:** Scribe (#12), Editor (#20).

---

### F. Tools and Integrations
- Search Engine Policy Knowledge Base.
- Industry Regulatory Manuals.

---

### G. Processing Logic
1. Receive candidate content or proposed site architecture change.
2. Evaluate against Google Spam Policies:
   - *Scraped Content Check:* Is value uniquely added with original first-party observations?
   - *Doorway Page Check:* Are multiple URLs created solely to funnel users to a single destination?
   - *Keyword Stuffing Check:* Does keyword insertion exceed natural readability thresholds?
3. Check EEAT compliance:
   - Are author qualifications or verified lab sources clearly stated?
4. Emit compliance verdict (`PASS` or `POLICY_VIOLATION_FLAG`).

---

### H. Outputs
- **Format:** Policy Audit Report JSON.
- **Example Output:**
```json
{
  "policy_audit_id": "pol_20261013_001",
  "status": "PASS",
  "spam_risk_score": "LOW",
  "eeat_rating": "STRONG",
  "violations_detected": [],
  "notes": "Original laboratory specification tables satisfy Google's information gain criteria."
}
```

---

### I. Inter-Agent Communication
- **Collaborates With:** Sentinel (#3) (during verification gate).
- **Advises:** Editor (#20) (during content planning).

---

### J. Memory and Persistence
- **Reads:** Negative constraints and search policies.
- **Writes:** Logs policy evaluations to audit history.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Policy analysis and advisory flags).

---

### L. Error Handling
- **Ambiguous Policy Change:** Issues warning and escalates to human review rather than guessing search engine intent.

---

### M. Evaluation
- Validated against test cases of known Google policy updates (e.g. March 2024 core update spam rules).

---

### N. Limitations
- Google search policies contain subjective quality thresholds; Scholar applies conservative risk boundaries.

---

### O. Extension Guide
To add vertical-specific advertising or legal restrictions (e.g. healthcare, legal services), add rules to `knowledge-bank/negative-constraints.json`.

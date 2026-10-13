# Agent Specification: Beacon (#9)
## AI Citation & LLM Mentions Specialist

```
========================================================================================
AGENT SPECIFICATION — BEACON
========================================================================================
```

### A. Identity
- **Agent Name:** Beacon
- **Agent ID:** `agent_beacon`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `schemas/v3_1/ai_visibility.json`

---

### B. Purpose
Beacon monitors whether the business is cited, referenced, and recommended as an authoritative source in Generative AI search systems, including **Google AI Overviews**, **Perplexity AI**, **ChatGPT Search**, and **Microsoft Copilot**.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Tracking presence of AI Overviews on target commercial SERPs.
  - Recording whether our URLs or competitor URLs are cited in generative answers.
  - Computing AI Sourceability Scores per landing page (evaluating if page copy is extractable by LLMs).
  - Monitoring `/llms.txt` and semantic citation endpoints.
- **Out of Scope (Does Not Own):**
  - Drafting AEO direct-answer blocks (owned by Answerer).
  - Traditional organic keyword rank tracking (owned by Scout).

---

### D. Capabilities
- **Verified Capabilities:**
  - Detection of `ai_overview_present` in DataForSEO SERP snapshots.
  - Logging of competitor domains cited inside AI Overviews.
  - Scoring page content for machine extractability (direct definitions, tables, Q&A blocks).
- **Partially Implemented:**
  - Automated programmatic query evaluation across ChatGPT Search and Perplexity APIs.
- **Planned Capabilities:**
  - Real-time alerts when a competitor displaces our brand citation in Google AI Overviews.

---

### E. Inputs
- **Required Context:** Priority commercial query list; target domain URLs.
- **Trigger Conditions:** Weekly AI visibility tracking cycle.
- **Upstream Dependencies:** Scout (SERP snapshots).

---

### F. Tools and Integrations
- `DataForSEO SERP API`: AI Overview detection and citation URL extraction.
- `AI Visibility Engine`: Computes extractability metrics.

---

### G. Processing Logic
1. For each target commercial query, check if an AI Overview is present.
2. If present, extract all cited external URLs and source domains.
3. Record if our domain is cited (`cited: true` or `cited: false`).
4. Record all cited competitor domains.
5. If not cited, evaluate our target landing page:
   - Check if page contains clear 2-sentence direct answer definition.
   - Check if page contains structured comparison table.
   - If missing, emit recommendation to Answerer (#14).
6. Emit structured `AI_VISIBILITY` record.

---

### H. Outputs
- **Format:** Structured JSON conforming to `AI_VISIBILITY`.
- **Schema:** `schemas/v3_1/ai_visibility.json`
- **Example Output:**
```json
{
  "visibility_id": "ai_20261013_kw091",
  "query": "cut wire shot vs steel grit shot peening",
  "platform": "GOOGLE_AI_OVERVIEW",
  "country": "US",
  "date": "2026-10-13",
  "mentioned": true,
  "cited": true,
  "citation_url": "https://suntecenterprises.com/blogs/cut-wire-shot-vs-steel-grit",
  "competitors_mentioned": ["Winoa", "Ervin Industries"],
  "answer_type": "COMPARISON_TABLE",
  "observation_method": "API",
  "confidence": "HIGH"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor (Pool A).
- **Feeds Into:** Answerer (#14) (to optimize direct answers), Editor (#20).

---

### J. Memory and Persistence
- **Reads:** Priority queries from Knowledge Bank.
- **Writes:** Stores `AI_VISIBILITY` records in database/JSON.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Read-only monitoring).

---

### L. Error Handling
- **Observation Uncertainty:** If citation presence cannot be verified with certainty, explicitly marks field as `cited: null` and `observation_method: NOT_MEASURABLE` (per Anti-Bullshit Standard).

---

### M. Evaluation
- Validated by comparing DataForSEO AI Overview responses against live visual SERP results.

---

### N. Limitations
- AI Overviews are personalized, dynamic, and geographically volatile; observations represent point-in-time regional snapshots.

---

### O. Extension Guide
To add monitoring for new generative engines, integrate their respective search APIs into the `AI Visibility Engine`.

# Agent Specification: Answerer (#14)
## AEO Direct-Answer & FAQ Structuring Specialist

```
========================================================================================
AGENT SPECIFICATION — ANSWERER
========================================================================================
```

### A. Identity
- **Agent Name:** Answerer
- **Agent ID:** `agent_answerer`
- **Functional Category:** Layer 4: Sequential Content Assembly Line (Pool B)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `schemas/v3_1/paa_question.json`

---

### B. Purpose
Answerer prepares content for **Answer Engine Optimization (AEO)** and **Generative Engine Optimization (GEO)**. It constructs concise 40-to-60-word direct-answer blocks, step-by-step engineering protocols, and structured FAQ accordions engineered specifically for Google Featured Snippets, Google AI Overviews, and LLM citation retrieval.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Drafting concise 2-sentence direct answer callouts immediately following question headings.
  - Formatting ordered lists for process/procedural queries.
  - Structuring FAQ accordions answering high-intent PAA questions.
  - Optimizing content for LLM machine-extractability.
- **Out of Scope (Does Not Own):**
  - Narrative body drafting (owned by Scribe).
  - Generating JSON-LD schemas (owned by Schema Master).
  - Verifying factual accuracy (owned by Sentinel).

---

- **Verified Capabilities:**
  - **Passage-Level Answerability Analysis (`PassageAnswerabilityAnalyzer`):** Chunks page content into semantic passages (40–80 words) and scores answerability based on entity-first syntax, factual number/tolerance density, conciseness, and zero preamble. Automatically detects Answerability Gaps against live Google PAA queries (`scripts/search_intelligence_engine.py`).
  - Structuring high-probability Featured Snippet answer blocks (40–60 words, inverted pyramid style).
  - FAQ accordion copy generation answering verified PAA questions.
  - Formatting comparison tables and technical tolerance lists.
- **Partially Implemented:**
  - Entity-dense semantic triples formatting for Knowledge Graph grounding.
- **Planned Capabilities:**
  - Voice-search natural language answer optimization.

---

### E. Inputs
- **Required Context:** Tuned Markdown draft from Tuner; target PAA questions from Editor's brief.
- **Trigger Conditions:** Tuner handoff.
- **Upstream Dependencies:** Tuner (#13), Editor (#20).

---

### F. Tools and Integrations
- `AEO Formatting Engine`: Evaluates snippet extractability.
- `PAA Question Bank`: Clustered question inventory.

---

### G. Processing Logic
1. Receive tuned draft from Tuner.
2. Locate core informational questions within draft H2/H3 headers.
3. Beneath each question heading, insert an authoritative direct answer block:
   - *Sentence 1:* Direct, definitive answer stating the core fact or conclusion.
   - *Sentence 2:* Qualifying specification, tolerance, or operational context.
   - Word count strictly between 40 and 60 words.
4. For procedural questions ("how to peen automotive springs" or "how to travel from Chandigarh to Dharampur"):
   - Structure an ordered list (`1.`, `2.`, `3.`) with bold imperative verbs.
5. Append an FAQ accordion section answering remaining secondary PAA queries.
6. Hand off enhanced draft to Schema Master (#15).

---

### H. Outputs
- **Format:** Enhanced Markdown with direct-answer callouts and FAQ blocks.
- **Downstream Consumer:** Schema Master (#15).

---

### I. Inter-Agent Communication
- **Receives From:** Tuner (#13).
- **Handoff To:** Schema Master (#15) (third station in Pool B pipeline).

---

### J. Memory and Persistence
- **Reads:** `PAA_QUESTION` targets from `CONTENT_BRIEF`.
- **Writes:** Updates internal draft snapshot with direct-answer markup.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Draft enhancement within memory).

---

### L. Error Handling
- **Fact Uncertainty in Direct Answer:** If an exact direct answer is ungrounded in Archivist, Answerer pauses and alerts Sentinel rather than synthesizing plausible text.

---

### M. Evaluation
- Evaluated on whether direct-answer blocks win Google Featured Snippets and trigger citations in Google AI Overviews.

---

### N. Limitations
- Does not guarantee snippet capture; Google algorithmically determines snippet display based on authority and query intent.

---

### O. Extension Guide
To tailor answer formats for new verticals, adjust snippet length templates in the `AEO Formatting Engine`.

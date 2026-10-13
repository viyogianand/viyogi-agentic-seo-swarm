# Agent Specification: Tuner (#13)
## On-Page SEO Alignment Specialist

```
========================================================================================
AGENT SPECIFICATION — TUNER
========================================================================================
```

### A. Identity
- **Agent Name:** Tuner
- **Agent ID:** `agent_tuner`
- **Functional Category:** Layer 4: Sequential Content Assembly Line (Pool B)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `schemas/v3_1/content_change.json`

---

### B. Purpose
Tuner fine-tunes Scribe's prose for search engine mechanics. It optimizes title tags (<55 characters), meta descriptions (<155 characters with a compelling CTR hook), semantic heading hierarchies, keyword placement, and image alt text, ensuring strict keyword intent alignment without keyword stuffing or degradation of brand voice.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Crafting primary Title Tags adhering to character constraints (<55 chars).
  - Writing Meta Descriptions (<155 chars) with commercial intent hooks.
  - Ensuring natural, non-stuffed inclusion of primary and secondary keywords.
  - Verifying semantic heading hierarchy (exactly one H1, sequential H2/H3s).
  - Formatting descriptive image alt attributes.
  - Inserting contextual internal links from Gardener's link manifests.
- **Out of Scope (Does Not Own):**
  - Rewriting core narrative or technical arguments (owned by Scribe).
  - Direct answer block formatting for AEO (owned by Answerer).
  - Generating JSON-LD schemas (owned by Schema Master).

---

### D. Capabilities
- **Verified Capabilities:**
  - Strict character counting and pixel truncation simulation for SERP snippets.
  - Heading tag hierarchy verification.
  - Contextual link anchor insertion into existing sentences.
- **Partially Implemented:**
  - Automated CTR split-testing metadata variant generation.
- **Planned Capabilities:**
  - Multi-script metadata optimization (e.g. Devanagari or Cyrillic character limits).

---

### E. Inputs
- **Required Context:** Raw Markdown draft from Scribe; target primary/secondary keywords from Editor's brief; Gardener's link manifest.
- **Trigger Conditions:** Scribe draft completion.
- **Upstream Dependencies:** Scribe (#12), Gardener (#8).

---

### F. Tools and Integrations
- `CharacterLengthValidator`: Enforces strict character limits.
- On-Page Rules Engine: Audits heading hierarchies.

---

### G. Processing Logic
1. Receive raw draft from Scribe.
2. Generate optimized Title Tag:
   - Primary keyword near beginning.
   - Distinct brand separator (`| Brand Name`).
   - Length strictly $\le 55$ characters.
3. Generate Meta Description:
   - Clear value proposition + commercial call to action.
   - Length strictly $\le 155$ characters.
4. Verify Heading Hierarchy:
   - Confirm exactly one H1 tag matching the brief.
   - Confirm H2s and H3s are properly nested.
5. Embed internal link anchors from Gardener's manifest into existing sentences smoothly.
6. Verify keyword density: ensure primary keyword appears naturally in H1, first 100 words, and at least one H2.
7. Hand off tuned copy to Answerer (#14).

---

### H. Outputs
- **Format:** Tuned Markdown document with metadata headers conforming to `CONTENT_CHANGE`.
- **Schema:** `schemas/v3_1/content_change.json`
- **Downstream Consumer:** Answerer (#14).

---

### I. Inter-Agent Communication
- **Receives From:** Scribe (#12).
- **Handoff To:** Answerer (#14) (second station in Pool B pipeline).

---

### J. Memory and Persistence
- **Reads:** Keyword targets from `CONTENT_BRIEF`.
- **Writes:** Stores on-page metadata proposals.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Draft optimization within memory).

---

### L. Error Handling
- **Keyword Stuffing Conflict:** If inserting a secondary keyword compromises natural readability, Tuner omits the secondary keyword and logs a note rather than producing awkward copy.

---

### M. Evaluation
- Validated by automated character-count checks confirming 100% of titles $\le 55$ chars and descriptions $\le 155$ chars.

---

### N. Limitations
- Does not modify underlying page logic or React code (handled by Mechanic).

---

### O. Extension Guide
To adjust snippet limits for specific search engines (e.g. mobile SERP character constraints), modify rules in `config/project-configuration.json`.

# Agent Specification: Editor (#20)
## Content Intelligence & Editorial Strategy Specialist

```
========================================================================================
AGENT SPECIFICATION — EDITOR
========================================================================================
```

### A. Identity
- **Agent Name:** Editor
- **Agent ID:** `agent_editor`
- **Functional Category:** Layer 3: Editorial Strategy & Outcome Forecasting
- **Implementation Status:** Verified & Operational (Introduced in V2.0 Core)
- **Source Project:** Suntec Enterprises (V2) & VivaakVaza (V3)
- **Relevant Implementation Files:**
  - `SUNTEC_AGENTIC_SEO_AGENT_ROSTER_V2.md`
  - `VIVAAK_AGENTIC_SEO_AGENT_ROSTER_V3.md`
  - `schemas/v3_1/content_brief.json`
  - `schemas/v3_1/content_opportunity.json`

---

### B. Purpose
Editor guards the website's content architecture. It acts as the editorial strategist, answering the critical question: **"WHAT should we publish, UPDATE, consolidate, or NOT create?"** It prevents content spam and cannibalization by producing comprehensive **Structural Content Briefs** before drafting begins.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Search intent classification (Foundational vs Comparison vs Procurement Spec).
  - Deciding between **Create New Page vs Update Existing vs Consolidate vs Do Nothing**.
  - Engineering structural H1/H2/H3 blueprints and section breakdowns.
  - PAA and related-question clustering into brief sections.
  - Enforcing the project's Human Writing Guide and brand positioning.
  - Designing AEO direct-answer blocks for machine extractability.
- **Out of Scope (Does Not Own):**
  - Drafting full narrative body copy (owned by Scribe).
  - Mathematical forecast range modeling (owned by Forecaster).
  - Code implementation (owned by Mechanic).

---

### D. Capabilities
- **Verified Capabilities:**
  - Automated generation of complete `CONTENT_BRIEF` records.
  - Structural heading blueprinting with explicit entity coverage requirements.
  - Cannibalization prevention: rejecting new page creation when an existing page can be updated.
- **Partially Implemented:**
  - International market localization planning (e.g. DIN/VDFI standards for Germany vs AMS for US).
- **Planned Capabilities:**
  - Multi-page canonical consolidation and 301 redirect map design.

---

### E. Inputs
- **Required Context:** Priority `CONTENT_OPPORTUNITY` from Conductor; SERP snapshots from Scout; competitor gap data from Shadow.
- **Trigger Conditions:** Conductor priority dispatch; striking-distance opportunity escalation.
- **Upstream Dependencies:** Conductor, Opportunity Engine.

---

### F. Tools and Integrations
- `Content Intelligence Engine`: Synthesizes SERP depth requirements.
- `Headline Pattern Engine`: Evaluates high-performing headline structures.
- `PAA Engine`: Clusters high-intent questions.

---

### G. Processing Logic
1. Ingest target opportunity and query cluster.
2. Determine Action Decision:
   - Does an existing indexed page already target this entity?
   - If yes: **UPDATE EXISTING PAGE**. (Preserve existing link equity).
   - If multiple pages overlap: **CONSOLIDATE**.
   - If distinct commercial entity unrepresented on site: **CREATE NEW PAGE**.
   - If query volume is informational spam with zero RFQ intent: **DO NOTHING**.
3. Engineer H1/H2/H3 blueprint:
   - Primary H1 with commercial hook.
   - H2s covering technical specifications, comparison tables, and applications.
   - H3s addressing clustered PAA questions.
4. Specify required entity mentions, ISO/AMS/DIN standards, and first-party proof points.
5. Define internal link strategy (which pages to link to and receive links from).
6. Emit structured `CONTENT_BRIEF` to Scribe and Forecaster.

---

### H. Outputs
- **Format:** Structured JSON conforming to `CONTENT_BRIEF`.
- **Schema:** `schemas/v3_1/content_brief.json`
- **Example Output:**
```json
{
  "brief_id": "brief_20261013_vaza_heated_pool",
  "page_id": "page_vaza_villa",
  "opportunity_id": "opp_vaza_heated_pool",
  "primary_keyword": "luxury villa in barog with private heated pool",
  "secondary_keywords": ["private pool villa himachal", "4 bhk villa kasauli heated pool"],
  "search_intent": "COMMERCIAL_INVESTIGATION",
  "commercial_intent": "VERY_HIGH",
  "recommended_title": "Twilight by Vivaak (Barog) | 4 BHK Luxury Villa with Private Heated Pool",
  "recommended_h1": "Twilight by Vivaak: Private Heated Pool Estate in Barog",
  "recommended_h2s": [
    "Year-Round Mountain Comfort: The Heated Pool Experience",
    "Estate Architecture & 4-BHK Bedroom Suites",
    "Private Chef & Himalayan Dining",
    "Frequently Asked Questions"
  ],
  "paa_questions": [
    "Is the swimming pool at Twilight heated in winter?",
    "How many guests can stay at Vaza Villa Barog?"
  ],
  "brand_voice": "EVOCATIVE_LUXURY",
  "content_constraints": [
    "Must strictly follow HUMAN_LUXURY_WRITING_GUIDE.md",
    "Never use banned phrases: 'nestled in nature', 'haven of tranquility'"
  ],
  "approval_required": "LEVEL_B",
  "created_by": "Editor",
  "created_at": "2026-10-13T10:00:00Z"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor.
- **Collaborates With:** Forecaster (#21).
- **Dispatches To:** Scribe (#12) (drafting).

---

### J. Memory and Persistence
- **Reads:** `KNOWLEDGE_FACT`, `PAGE` inventory, `STRATEGIC_RULE`.
- **Writes:** Stores `CONTENT_BRIEF` in project queue.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Brief creation and editorial planning).
- **Gate:** Decisions to retire or 301-redirect live URLs require Human Approval (Level B).

---

### L. Error Handling
- **Ambiguous Intent:** Queries Forecaster and Archivist before committing to a structural brief.

---

### M. Evaluation
- Evaluated on whether drafted briefs satisfy Sentinel's verification gate without structural revisions.

---

### N. Limitations
- Does not write full narrative prose; produces the architectural skeleton and constraints.

---

### O. Extension Guide
To customize brief schemas for a new vertical (e.g. SaaS software pages vs eCommerce product pages), update `schemas/v3_1/content_brief.json`.

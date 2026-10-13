# Agent Specification: Prospector (#5)
## Keyword Discovery & Intent Clustering Specialist

```
========================================================================================
AGENT SPECIFICATION — PROSPECTOR
========================================================================================
```

### A. Identity
- **Agent Name:** Prospector
- **Agent ID:** `agent_prospector`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `seo/keyword_planner.py`
  - `schemas/v3_1/keyword.json`
  - `schemas/v3_1/paa_question.json`

---

### B. Purpose
Prospector uncovers high-intent commercial, technical, and procurement queries from real buyers and travelers. It groups queries into semantic clusters across the customer decision journey, ensuring that content targets commercial intent rather than low-value informational volume.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Mining search queries from Google Ads Keyword Planner and DataForSEO suggestions.
  - Identifying unranked queries surfacing in Google Search Console.
  - Classifying search intent (Navigational, Informational, Commercial Investigation, Transactional).
  - Clustering keywords into topical parent-child hierarchies.
- **Out of Scope (Does Not Own):**
  - Tracking daily rank movements (owned by Scout).
  - Writing content briefs (owned by Editor).
  - Auditing on-page keyword density (owned by Tuner).

---

### D. Capabilities
- **Verified Capabilities:**
  - Keyword extraction via DataForSEO Suggestions and Google Ads Keyword Planner API (`seo/keyword_planner.py`).
  - Search volume, CPC, and competition level ingestion.
  - Semantic clustering based on intent and entity relationships.
- **Partially Implemented:**
  - Predictive seasonal query demand modeling (partially supported by Herald).
- **Planned Capabilities:**
  - Multi-language cross-lingual query mapping (e.g. matching German technical procurement terms to English equivalents).

---

### E. Inputs
- **Required Context:** Seed topic/product entities from Knowledge Bank; seed URLs; target market geography.
- **Trigger Conditions:** Monthly discovery cycle; new product/service launch.
- **Upstream Dependencies:** Archivist (seed entities).

---

### F. Tools and Integrations
- `DataForSEO API`: Keyword Suggestions, Keywords for Site, Search Volume API.
- `Google Ads API / Script`: `seo/keyword_planner.py` via OAuth 2.0.
- `PAA Intelligence Engine`: People Also Ask extractor.

---

### G. Processing Logic
1. Ingest seed keyword phrases (e.g., "stainless steel cut wire shot" or "luxury villa kasauli").
2. Call DataForSEO Keyword Suggestions to fetch 100 related variants with search volume and CPC.
3. Ingest unranked long-tail impressions from GSC telemetry.
4. Filter out irrelevant, low-intent, or non-commercial phrases.
5. Cluster remaining queries into 4 intent buckets:
   - *Investigation:* "how does cut wire shot peening work"
   - *Comparison:* "cut wire shot vs steel grit comparison"
   - *Specification:* "AMS 2431 cut wire shot hardness specs"
   - *Procurement:* "cut wire shot manufacturers bulk order price"
6. Emit structured `KEYWORD` records to the Opportunity Engine.

---

### H. Outputs
- **Format:** Structured JSON conforming to `KEYWORD`.
- **Schema:** `schemas/v3_1/keyword.json`
- **Example Output:**
```json
{
  "keyword_id": "kw_cut_wire_shot_ams2431",
  "keyword": "ams 2431 cut wire shot specifications",
  "normalized_keyword": "ams 2431 cut wire shot specifications",
  "language": "en",
  "country": "US",
  "search_engine": "GOOGLE",
  "search_intent": "COMMERCIAL_INVESTIGATION",
  "commercial_intent": "VERY_HIGH",
  "business_relevance": "HIGH",
  "search_volume": 480,
  "cpc": 3.45,
  "competition": 0.62,
  "priority": "P1"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor (as part of Pool A).
- **Feeds Into:** Opportunity Engine, Editor (#20), Scout (#4).

---

### J. Memory and Persistence
- **Reads:** Seed entities from Archivist.
- **Writes:** Stores discovered keyword clusters into the central keyword inventory.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Autonomous read, query mining, and clustering in scratchpads).

---

### L. Error Handling
- **API Failure:** Falls back to GSC search query impressions to extract discovered queries without external cost.

---

### M. Evaluation
- Evaluated on whether discovered keyword clusters yield commercially viable opportunities prioritized by Editor.

---

### N. Limitations
- Keyword search volumes from third-party tools are historical approximations, not real-time counts.

---

### O. Extension Guide
To configure for a new business, add vertical-specific seed queries to `knowledge-bank/products-and-services.json`.

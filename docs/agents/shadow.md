# Agent Specification: Shadow (#6)
## Competitor Deconstruction & Content Gap Specialist

```
========================================================================================
AGENT SPECIFICATION — SHADOW
========================================================================================
```

### A. Identity
- **Agent Name:** Shadow
- **Agent ID:** `agent_shadow`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `schemas/v3_1/competitor.json`
  - `schemas/v3_1/content_gap.json`

---

### B. Purpose
Shadow monitors competitors' digital footprints. It deconstructs their website architecture, newly published pages, heading hierarchies, specification tables, and ranking advantages, exposing content gaps that our swarm can exploit.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Scraping public competitor markup and heading structures (H1–H3).
  - Comparing competitor page depth, word count, and schema against target pages.
  - Identifying missing topics, technical specs, or FAQs where competitors outrank us.
  - Maintaining the Competitor Intelligence Matrix.
- **Out of Scope (Does Not Own):**
  - Scraping private or password-protected content.
  - Analyzing competitor backlinks (owned by Envoy).
  - Writing the competitive response content (owned by Editor & Scribe).

---

### D. Capabilities
- **Verified Capabilities:**
  - Structured extraction via Firecrawl API and Python `RobustHTMLParser`.
  - Heading hierarchy comparison (our page vs #1 ranking competitor).
  - Identification of structured data gaps (e.g., competitor has `Product` schema, we do not).
- **Partially Implemented:**
  - Automated diffing of competitor pricing and commercial terms.
- **Planned Capabilities:**
  - Automated detection of competitor site redesigns and 301 redirect migrations.

---

### E. Inputs
- **Required Context:** List of verified competitor domains from Knowledge Bank (`knowledge-bank/competitors.json`); target URLs.
- **Trigger Conditions:** Bi-weekly competitive crawl; sudden drop in ranking behind a specific competitor.
- **Upstream Dependencies:** Archivist (competitor domains).

---

### F. Tools and Integrations
- `Firecrawl API`: Fetches clean Markdown, stripped of navigation/scripts.
- `DataForSEO Domain Intersection API`: Exposes keywords where competitors rank in top 10 but we do not.
- Python `RobustHTMLParser`: Extracts headings and metadata.

---

### G. Processing Logic
1. Identify URLs where a tracked competitor ranks higher for our target keyword.
2. Scrape competitor URL using Firecrawl or lightweight HTTP fetch.
3. Extract structural blueprint: Title, Meta, H1, H2 list, H3 list, word count, schema types.
4. Compare against our existing landing page for the same topic.
5. Identify explicit gaps:
   - *Topic Gap:* Competitor covers "vibration resistance" or "bonfire amenities"; we do not.
   - *Structural Gap:* Competitor has comparison table; we have generic paragraphs.
   - *Schema Gap:* Competitor has rich snippet FAQ; we have raw text.
6. Emit structured `CONTENT_GAP` records.

---

### H. Outputs
- **Format:** Structured JSON conforming to `CONTENT_GAP`.
- **Schema:** `schemas/v3_1/content_gap.json`
- **Example Output:**
```json
{
  "gap_id": "gap_20261013_winoa_h2",
  "page_id": "page_cut_wire_shot",
  "gap_type": "MISSING_TOPIC",
  "description": "Competitor Winoa ranks #1; includes detailed VDFI 8001 conditioning tolerance table.",
  "evidence": "Winoa URL /cut-wire-shot has H2 'Conditioned vs As-Cut Wire Shot Tolerances' with 480-word spec table.",
  "competitor_evidence": ["winoagroup.com/products/cut-wire-shot"],
  "business_value": "HIGH",
  "seo_value": 85.0,
  "effort": "LOW",
  "confidence": "HIGH",
  "priority": "P1",
  "recommended_action": "Add VDFI 8001 conditioning grade tolerance table to /cut-wire-shot page.",
  "status": "OPEN"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor (Pool A).
- **Feeds Into:** Editor (#20), Opportunity Engine.

---

### J. Memory and Persistence
- **Reads:** Competitor domains from Archivist.
- **Writes:** Caches scraped competitor heading structures with a 14-day TTL.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Autonomous read of public web pages).
- **Prohibited:** Never bypasses `robots.txt` or attempts to access non-public systems.

---

### L. Error Handling
- **Scraper Blocked / 403 Forbidden:** Falls back to parsing public Google SERP descriptions and cached text snippets via DataForSEO.

---

### M. Evaluation
- Evaluated on the precision of identified content gaps confirmed by Editor in subsequent content briefs.

---

### N. Limitations
- Cannot evaluate competitor bounce rates or internal conversion rates (categorized as `Evidence State: UNKNOWN`).

---

### O. Extension Guide
To track new competitors, update `knowledge-bank/competitors.json` with domain names and primary target product URLs.

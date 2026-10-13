# Agent Specification: Schema Master (#15)
## Structured Data & JSON-LD Architect

```
========================================================================================
AGENT SPECIFICATION — SCHEMA MASTER
========================================================================================
```

### A. Identity
- **Agent Name:** Schema Master
- **Agent ID:** `agent_schema_master`
- **Functional Category:** Layer 4: Sequential Content Assembly Line (Pool B)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `schemas/v3_1/structured_data.json`

---

### B. Purpose
Schema Master engineers valid, rich, and error-free **JSON-LD structured data**. It establishes explicit entity relationships in the Google Knowledge Graph and search engines, synchronizing machine-readable schemas (`Organization`, `Product`, `Hotel`, `FAQPage`, `BreadcrumbList`) perfectly with visible page copy.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Generating Schema.org-compliant JSON-LD script blocks.
  - Ensuring 100% synchronization between schema fields and on-page text (preventing cloaking or schema mismatch penalties).
  - Linking entity nodes via unambiguous `@id` URIs.
  - Formatting `FAQPage`, `BreadcrumbList`, `LocalBusiness`, and vertical-specific schemas (`Product` / `LodgingBusiness`).
- **Out of Scope (Does Not Own):**
  - Drafting copy (owned by Scribe).
  - Vetoing schemas for factual errors (owned by Sentinel).
  - Injecting schemas into Next.js React layout files (owned by Mechanic).

---

### D. Capabilities
- **Verified Capabilities:**
  - Generation of complete, nested JSON-LD schema objects.
  - Full support for `Organization`, `WebSite`, `BreadcrumbList`, `FAQPage`, `Product`, `LodgingBusiness`, `HotelRoom`.
  - Geo-coordinates and Plus Code enrichment.
- **Partially Implemented:**
  - Multi-item collection and carousel schema modeling.
- **Planned Capabilities:**
  - Automated JSON-LD validation against Google Rich Results Test API via headless runner.

---

### E. Inputs
- **Required Context:** Assembled draft from Answerer; entity definitions and geo-coordinates from Archivist; page URL and canonical route.
- **Trigger Conditions:** Answerer handoff.
- **Upstream Dependencies:** Answerer (#14), Archivist (#2).

---

### F. Tools and Integrations
- `JSON-LD Architect`: Validates syntax, required properties, and `@context`.
- Schema.org vocabulary registry.

---

### G. Processing Logic
1. Receive complete draft with FAQ blocks from Answerer.
2. Determine required schema types based on page type:
   - *B2B Industrial Page:* `Product`, `TechnicalArticle`, `FAQPage`, `BreadcrumbList`.
   - *Hospitality Page:* `LodgingBusiness`, `HotelRoom`, `FAQPage`, `BreadcrumbList`.
   - *Sitewide Layout:* `Organization`, `WebSite`.
3. Construct canonical JSON-LD script blocks.
4. Extract all FAQ questions and answers from visible text:
   - Strictly match `FAQPage.mainEntity` text to visible on-page copy.
5. Link `@id` properties to canonical website URLs.
6. Package complete draft and JSON-LD bundle for Sentinel (#3) verification.

---

### H. Outputs
- **Format:** Valid JSON-LD script blocks embedded within Markdown or standalone JSON.
- **Schema:** `schemas/v3_1/structured_data.json`
- **Example Output:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is the swimming pool at Twilight by Vivaak heated in winter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, Twilight by Vivaak features a private, temperature-controlled heated plunge pool designed for year-round comfort, including winter mountain temperatures in Barog."
      }
    }
  ]
}
```

---

### I. Inter-Agent Communication
- **Receives From:** Answerer (#14).
- **Handoff To:** Sentinel (#3) (terminal verification station of Pool B).

---

### J. Memory and Persistence
- **Reads:** Entity definitions and geo-coordinates from Archivist.
- **Writes:** Attaches structured data blocks to the candidate release package.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Schema generation within memory).

---

### L. Error Handling
- **Missing Required Schema Property:** Automatically queries Archivist for required fallback field; if unavailable, omits optional fields rather than generating invalid types.

---

### M. Evaluation
- Evaluated on whether generated schemas achieve 0 errors and 0 warnings on Google Rich Results tests.

---

### N. Limitations
- Does not guarantee rich snippet display; Google displays rich results based on authority and relevance algorithms.

---

### O. Extension Guide
To add support for new Schema.org types (e.g. `SoftwareApplication`, `MedicalWebPage`), add type definitions to the `JSON-LD Architect`.

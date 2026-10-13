# Knowledge Bank Configuration Guide
## Configuring Business Facts, Specifications, Voice Guidelines & Entity Mappings

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — KNOWLEDGE BANK SPECIFICATION
========================================================================================
```

## 1. Overview & Purpose

The **Knowledge Bank** is the single source of truth for all business-specific information in the Viyogi Agentic SEO Swarm. It completely decouples company-specific facts from the reusable multi-agent reasoning logic.

When configuring the swarm for a new business, developers and operators populate the files in `knowledge-bank/`. The core agents (Conductor, Sentinel, Scribe, Tuner) read from this directory to ground all strategy, writing, and verification without modifying agent code or prompts.

---

## 2. Standard Knowledge Bank File Structure

A fully configured project Knowledge Bank contains the following structured files:

```
knowledge-bank/
├── brand-identity.json          # Legal entity, brand name, locations, NAP, social links
├── products-and-services.json   # Catalog of products, services, specs, features, tolerances
├── entities-and-relations.json  # Semantic entity graph (Products ➔ Standards ➔ Applications)
├── competitors.json             # Tracked competitor domains, primary strengths/weaknesses
├── human-writing-guide.md       # Brand voice, style rules, and banned marketing buzzwords
├── standards-and-claims.json    # Certifications, verified lab claims, compliance standards
└── negative-constraints.json    # Prohibited claims, sensitive topics, off-limit keywords
```

---

## 3. Template Specifications & Schema Definitions

### 3.1 Brand Identity (`brand-identity.json`)
Defines foundational entity facts:
```json
{
  "entity_id": "ent_brand_master",
  "brand_name": "Suntec Enterprises",
  "legal_name": "Suntec Enterprises Private Limited",
  "founding_year": 2001,
  "headquarters": {
    "street_address": "Sector 49, Industrial Area",
    "city": "Faridabad",
    "state": "Haryana",
    "postal_code": "121001",
    "country": "India",
    "latitude": 28.3756,
    "longitude": 77.2984,
    "plus_code": "9F83+4V Faridabad, Haryana"
  },
  "official_phone": "+91-98110-XXXXX",
  "official_email": "info@suntecenterprises.com",
  "website_url": "https://suntecenterprises.com",
  "google_business_profile_url": "https://maps.google.com/?cid=1234567890",
  "social_links": {
    "linkedin": "https://www.linkedin.com/company/suntec-enterprises",
    "youtube": "https://www.youtube.com/@suntecenterprises"
  }
}
```

### 3.2 Products & Services (`products-and-services.json`)
Defines the authoritative catalog with exact specifications:
```json
{
  "catalog_version": "2026.1",
  "items": [
    {
      "item_id": "prod_cut_wire_shot_ss",
      "canonical_name": "Stainless Steel Cut Wire Shot",
      "short_name": "SS Cut Wire Shot",
      "category": "Metallic Abrasives",
      "grades": ["Conditioned (G1, G2, G3)", "As-Cut"],
      "specifications": {
        "hardness": "45-52 HRC / 50-60 HRC",
        "density": "7.8 g/cm³",
        "durability_cycles": "4,500 - 5,000 cycles",
        "chemical_composition": {
          "carbon": "0.15 - 0.25%",
          "chromium": "17.0 - 19.0%",
          "nickel": "8.0 - 10.0%"
        }
      },
      "applicable_standards": ["AMS 2431/8", "SAE J441", "DIN 8201", "VDFI 8001"],
      "primary_applications": [
        "Automotive suspension spring peening",
        "Aerospace turbine blade treatment",
        "Stainless steel foundry deburring"
      ]
    }
  ]
}
```

### 3.3 Human Writing Guide (`human-writing-guide.md`)
Defines the brand tone and **strict negative constraints** enforced by Sentinel:
```markdown
# Brand Writing Guide & Style Constitution

## 1. Core Voice & Tone
- Tone is authoritative, engineering-first, factual, and direct.
- Explain the "how" and "why" behind specifications immediately.
- Use metric and imperial units in parallel (e.g. 7.8 g/cm³ [0.282 lb/in³]).

## 2. Zero-Tolerance Banned Buzzwords
The following terms are strictly banned from all drafts. Sentinel will veto any text containing:
- "In today's fast-paced world"
- "Revolutionizing the industry"
- "State-of-the-art technology"
- "Game-changer"
- "Testament to our commitment"
- "Nestled in the heart of"
- "Look no further"
- "Beacon of excellence"

## 3. Structural Rules
- Always lead with a 2-sentence direct answer.
- All technical comparisons must be formatted as Markdown tables.
- Keep title tags under 55 characters; meta descriptions under 155 characters.
```

---

## 4. Completeness Validation Protocol

Before launching an operational cycle, the system verifies Knowledge Bank completeness:
1. Run the validator:
   ```bash
   python3 -m schemas.v3_1.validator --check-knowledge-bank
   ```
2. The validator verifies that:
   - All required fields in `brand-identity.json` and `products-and-services.json` are present and non-null.
   - All references to standards resolve to valid entities in `standards-and-claims.json`.
   - Geo-coordinates parse as valid decimals.
3. If errors are found, the swarm halts execution and highlights missing fields.

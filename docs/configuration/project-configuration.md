# Project Configuration Guide
## Onboarding a New Business to Viyogi Agentic SEO Swarm

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — PROJECT CONFIGURATION GUIDE
========================================================================================
```

## 1. Overview

Configuring the swarm for a new business involves creating a dedicated project directory with two components:
1. **Layer B: Project Configuration (`config/project-configuration.json`):** Environment IDs, connected APIs, enabled agents, and execution parameters.
2. **Layer C: Knowledge Bank (`knowledge-bank/`):** Verified business facts, product catalogs, competitor domains, and writing style guides.

---

## 2. Step-by-Step Onboarding Process

```mermaid
flowchart TD
    STEP1[1. Initialize Project Directory<br/>mkdir my-business-seo] --> STEP2[2. Copy Template Files<br/>from templates/ or examples/]
    STEP2 --> STEP3[3. Configure project-configuration.json<br/>Domain, Property IDs, Market Codes]
    STEP3 --> STEP4[4. Populate Knowledge Bank<br/>Specs, Claims, Writing Guide]
    STEP4 --> STEP5[5. Configure Credentials (.env.local)<br/>DataForSEO, Google OAuth, Bing Key]
    STEP5 --> STEP6[6. Run Schema & Fact Validator<br/>python3 validator.py --check-all]
    STEP6 --> STEP7[7. Execute Baseline Crawl & Audit<br/>python3 run_phase1_intelligence.py]
```

---

## 3. Configuration Template (`project-configuration.json`)

```json
{
  "project_id": "suntec-enterprises-prod",
  "project_name": "Suntec Enterprises Growth System",
  "domain": "https://suntecenterprises.com",
  "business_type": "B2B_MANUFACTURING",
  "target_markets": [
    {"country": "IN", "language": "en", "priority": "P0"},
    {"country": "DE", "language": "en", "priority": "P1"},
    {"country": "US", "language": "en", "priority": "P1"}
  ],
  "storage_adapter": "CLOUDFLARE_D1",
  "governance": {
    "level_b_approval_required": true,
    "level_c_approval_required": true,
    "approval_queue_file": "APPROVAL_QUEUE.md"
  },
  "concurrency_limits": {
    "pool_a_max_workers": 5,
    "pool_b_max_workers": 1,
    "pool_c_max_workers": 1
  },
  "connected_services": {
    "dataforseo_enabled": true,
    "gsc_enabled": true,
    "ga4_enabled": true,
    "bing_webmaster_enabled": true,
    "indexnow_enabled": true,
    "google_indexing_api_enabled": true,
    "google_business_profile_enabled": true
  },
  "cadence": {
    "pool_a_intelligence": "0 2 * * 1",
    "monthly_executive_report": "0 6 1 * *"
  }
}
```

---

## 4. Adapting Across Industry Verticals

The framework natively adapts to different business verticals by adjusting the `business_type` and Knowledge Bank schemas:

| Vertical | Primary North Star | Primary Schema.org Types | Key Writing Guide Emphasis |
| :--- | :--- | :--- | :--- |
| **Industrial Manufacturing** | Qualified RFQs, bulk orders | `Product`, `TechnicalArticle`, `Organization` | Material composition, ASTM/DIN standards, tolerances, capacity. |
| **Boutique Hospitality & Villas** | Direct bookings, WhatsApp inquiries | `LodgingBusiness`, `HotelRoom`, `FAQPage` | Sensory immersion, heated amenities, privacy, local geography. |
| **B2B SaaS** | Free trial signups, demo requests | `SoftwareApplication`, `FAQPage` | Feature comparison tables, integrations, security compliance. |
| **Local Professional Services** | Phone calls, appointment bookings | `LocalBusiness`, `Service`, `FAQPage` | Verified credentials, service areas, customer testimonials. |

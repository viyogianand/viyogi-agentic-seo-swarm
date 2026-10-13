# Memory Architecture & Knowledge Bank
## 4-Level Strategic Memory, Knowledge Bank & Fact Verification

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — MEMORY & KNOWLEDGE SPECIFICATION
========================================================================================
```

## 1. The 4-Level Strategic Memory Model

A major failure mode in traditional agentic systems is the "amnesiac loop" — agents rediscovering the same insights, repeating failed experiments, or hallucinating business facts.

The Viyogi framework resolves this by implementing a **4-Level Bayesian Strategic Memory Model** maintained by **Archivist**:

```
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL 4: STRATEGIC RULES (Codified Strategic Policy)                   │
│ • Heuristics validated across multiple 28-day experiments.             │
│ • Example: "For this domain, technical comparison tables achieve 3.4x  │
│   higher CTR than FAQ accordions for procurement queries."             │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ Promoted after repeated validation
┌───────────────────────────────────┴────────────────────────────────────┐
│ LEVEL 3: CAUSAL LEARNINGS (Attributed Empirical Outcomes)              │
│ • Synthesized causal takeaways from completed experiments.             │
│ • Example: "Adding VDFI tolerance specs to Cut Wire Shot page moved    │
│   ranking from pos 14.2 to 5.8 in Germany within 21 days."             │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ Derived from measured telemetry
┌───────────────────────────────────┴────────────────────────────────────┐
│ LEVEL 2: EMPIRICAL OBSERVATIONS (Time-Series Evidence Stream)          │
│ • Discrete historical events recorded by Pool A intelligence.          │
│ • Example: "Competitor Winoa modified H2 tags on /cut-wire-shot URL;   │
│   gained position 2 for 'cut wire shot supplier'."                     │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ Grounded against
┌───────────────────────────────────┴────────────────────────────────────┐
│ LEVEL 1: GROUNDED BUSINESS FACTS (Immutable Single Source of Truth)    │
│ • Verified corporate specifications, product attributes, floor plans,  │
│   chemical compositions, pricing policies, and certifications.         │
│ • Zero inference permitted. Maintained with cryptographic fidelity.    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Knowledge Bank Architecture

The **Knowledge Bank** is the single source of truth for all business-specific information. It is strictly decoupled from the core framework and resides in `knowledge-bank/`:

```
knowledge-bank/
├── brand-identity.json          # Legal entity name, founders, year, locations, NAP
├── products-and-services.json   # Technical specs, catalog, tolerances, pricing tiers
├── entities-and-relations.json  # Knowledge graph linking Products ➔ Standards ➔ Locations
├── competitors.json             # Core competitor domains, tracked URLs, strengths/weaknesses
├── human-writing-guide.md       # Banned buzzwords, tone rules, structure guidelines
├── standards-and-claims.json    # Certifications (ISO/AMS/DIN), verified legal claims
└── negative-constraints.json    # Banned topics, sensitive claims, prohibited promises
```

### Knowledge Fact Schema (`KNOWLEDGE_FACT`)
Every fact stored in the Knowledge Bank conforms to the canonical RDF-style schema:
```json
{
  "id": "fact_cut_wire_shot_density",
  "record_type": "KNOWLEDGE_FACT",
  "subject": "Stainless Steel Cut Wire Shot",
  "predicate": "density",
  "object": "7.8 g/cm³",
  "entity_id": "ent_cut_wire_shot",
  "value": "7.8",
  "unit": "g/cm3",
  "source": "Lab Certificate Q4-2026 / ISO 11124-4",
  "source_url": "file:///ops/certificates/iso11124-4.pdf",
  "verified": true,
  "verification_status": "VERIFIED",
  "verified_by": "Metallurgical Lab Lead",
  "verified_at": "2026-09-10T14:00:00Z",
  "expires_at": null,
  "created_at": "2026-09-10T14:00:00Z",
  "updated_at": "2026-09-10T14:00:00Z"
}
```

---

## 3. Storage Adapters & Multi-Engine Persistence

To ensure the framework remains deployable across diverse environments, Archivist interacts with storage through a pluggable `StorageAdapter` interface:

| Environment | Primary Storage Adapter | Implementation Details |
| :--- | :--- | :--- |
| **Edge / Cloudflare (Suntec)** | `CloudflareD1Adapter` | SQLite relational database distributed across Cloudflare Edge nodes. Fast SQL queries for products, blogs, and inquiries. |
| **Serverless / Firebase (Vivaak)** | `FirebaseRTDBAdapter` | Realtime NoSQL document store. Synchronizes content versions, inquiries, and state snapshots. |
| **Local Antigravity Workspace** | `LocalJsonStorageAdapter` | Zero-dependency filesystem JSON storage in `data/` and `schemas/v3_1/`. Validated via `validator.py`. |
| **Enterprise Relational** | `PostgresStorageAdapter` | Standard PostgreSQL database for dedicated VPS/cloud container deployments. |

### Caching Policies & TTLs
To prevent excessive API calls and redundant model token usage, Archivist enforces tiered cache expirations:

| Data Type | Cache TTL | Rationale |
| :--- | :--- | :--- |
| **Verified Specifications & Claims** | Infinite (Until explicit update) | Physical metallurgy, estate floorplans, and ISO standards do not change unexpectedly. |
| **Competitor Page Markup Scrapes** | 14 Days | Competitors rarely overhaul core structural markup more than bi-weekly. |
| **SERP Snapshots & Rankings** | 7 Days | Weekly cadence prevents rate-limiting and captures genuine ranking trends. |
| **GSC / GA4 Telemetry Records** | 24 Hours | First-party streams are refreshed daily. |
| **Forecast Calibration Logs** | Permanent Immutable | Historical error records must never be purged to allow longitudinal accuracy tracking. |

---

## 4. Client Data Isolation & Sandboxing

When deploying Viyogi Agentic SEO Swarm across multiple clients:
1. **Zero Cross-Client Leakage:** Agents working on Client B have no access to Client A's Knowledge Bank, Strategic Memory, database credentials, or API keys.
2. **Strict Workspace Sandboxing:** Each business runs within an isolated environment directory containing its own `.env` and `knowledge-bank/`.
3. **No Centralized Cross-Tenant LLM Context:** Fact lookups are scoped strictly to the current workspace's Archivist store. Prompts never inject facts from other projects.

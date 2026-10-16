# Multi-Client Data Isolation & Security Architecture
## Zero-Leakage Tenancy, Cryptographic Sandboxing & Credential Boundaries

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — CLIENT ISOLATION SPECIFICATION
========================================================================================
```

## 1. The Core Threat Model: Cross-Client Contamination

In multi-client agency or enterprise deployments, the primary security risk is **Cross-Client Knowledge Contamination**:
- An agent writing copy for Client B (e.g. Luxury Resort) inadvertently injects proprietary specifications or pricing from Client A (e.g. Industrial Foundry).
- Analytics or Search Console credentials from one client are queried when analyzing another client's domain.
- Competitive intelligence or private lead submission logs are exposed in shared model contexts.

The Viyogi framework enforces **Four Hard Isolation Boundaries** to eliminate this risk.

---

## 2. The Four Isolation Boundaries

```
┌────────────────────────────────────────────────────────────────────────┐
│ BOUNDARY 1: WORKSPACE & DIRECTORY SANDBOXING                           │
│ • Client configurations live in dedicated, isolated directories.       │
│ • No shared `.env` files across distinct client environments.          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ enforced by
┌───────────────────────────────────▼────────────────────────────────────┐
│ BOUNDARY 2: KNOWLEDGE BANK ISOLATION                                   │
│ • Archivist (#2) strictly scopes queries to the local `knowledge-bank/`│
│ • Facts from Client A are never loaded into Client B's vector or cache.│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ enforced by
┌───────────────────────────────────▼────────────────────────────────────┐
│ BOUNDARY 3: CREDENTIAL & MCP DOMAIN VALIDATION                         │
│ • Prior to executing GSC/GA4/Bing API requests, the domain is verified.│
│ • Mismatched accounts are instantly blocked; no data is leaked.        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ enforced by
┌───────────────────────────────────▼────────────────────────────────────┐
│ BOUNDARY 4: ZERO LLM CONTEXT RESIDUALS                                 │
│ • Each agent turn initializes with a clean, deterministic system prompt│
│ • No multi-tenant shared memory services or persistent cross-run caches│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Epistemic Grounding Checks (Sentinel Veto)
Before any draft is approved:
- Sentinel (#19) compares discrete extracted assertions against `knowledge-bank/brand-identity.json` and `products-and-services.json`.
- If an entity, claim, or tolerance belongs to another entity or is unrecognized in local memory, the draft is vetoed immediately with status `REJECTED_UNKNOWN_ENTITY`.

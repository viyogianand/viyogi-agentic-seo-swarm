# Agent Specification: Archivist (#2)
## Single Source of Truth & 4-Level Strategic Memory

```
========================================================================================
AGENT SPECIFICATION — ARCHIVIST
========================================================================================
```

### A. Identity
- **Agent Name:** Archivist
- **Agent ID:** `agent_archivist`
- **Functional Category:** Layer 1: Governance & Strategic Brain
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises (D1 SQLite) & VivaakVaza (Firebase RTDB / JSON)
- **Relevant Implementation Files:**
  - `knowledge-bank/`
  - `schemas/v3_1/knowledge_fact.json`
  - `schemas/v3_1/strategic_rule.json`
  - `schemas/v3_1/learning.json`

---

### B. Purpose
Archivist serves as the **Single Source of Truth** for the entire swarm. It maintains immutable corporate facts, technical specifications, and the 4-level Strategic Memory, ensuring that agents never hallucinate specs or repeat failed experiments.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Indexing and retrieving verified corporate facts (`KNOWLEDGE_FACT`).
  - Managing the 4-Level Strategic Memory (Facts, Observations, Learnings, Strategic Rules).
  - Caching competitor structures, SERP snapshots, and historical experiment outcomes.
  - Serving fact lookup queries from Sentinel, Scribe, and Conductor.
- **Out of Scope (Does Not Own):**
  - Synthesizing new strategic actions (owned by Conductor).
  - Verifying if a draft matches the facts (owned by Sentinel).
  - Drafting content (owned by Scribe).

---

### D. Capabilities
- **Verified Capabilities:**
  - **Entity Salience & Graph Analysis (`EntitySalienceAnalyzer`):** Extracts named domain entities, evaluates structural prominence (URL slug, Title, H1, first 100 words), constructs formal RDF Knowledge Graph triples ($\text{Subject} \xrightarrow{\text{Predicate}} \text{Object}$), and cross-references page claims against verified facts in Strategic Memory (`scripts/search_intelligence_engine.py`).
  - High-speed key-value and entity relationship lookups against JSON/D1 stores.
  - Expiration-aware caching (7-day SERP TTL, infinite fact TTL).
  - Promotion logic: elevating repeated empirical findings into Level 4 Strategic Rules.
- **Partially Implemented:**
  - Vector similarity search across unstructured technical lab PDFs.
- **Planned Capabilities:**
  - Multi-tenant cryptographic namespace isolation for enterprise agencies.

---

### E. Inputs
- **Required Context:** Fact query with `subject`, `predicate`, or `entity_id`.
- **Trigger Conditions:** Called dynamically whenever any agent needs grounded facts.
- **Upstream Dependencies:** None (foundational data store).

---

### F. Tools and Integrations
- `StorageAdapter.query`: Direct SQL/JSON database querying.
- `KnowledgeBankReader`: Reads local files in `knowledge-bank/`.

---

### G. Processing Logic
1. Receive query for entity attribute (e.g. `subject: "Vaza Villa"`, `predicate: "heated_pool"`).
2. Query Level 1 Fact Store.
3. If verified record exists with `status: VERIFIED`, return record with high confidence.
4. If record is unverified or conflicting, return `status: UNVERIFIED` and flag for human review.
5. Provide contextual learnings from Level 3 memory relating to the entity.

---

### H. Outputs
- **Format:** Structured JSON conforming to `KNOWLEDGE_FACT`.
- **Schema:** `schemas/v3_1/knowledge_fact.json`
- **Example Output:**
```json
{
  "fact_id": "fact_0492_ams2431",
  "subject": "AMS 2431/8",
  "predicate": "hardness_specification",
  "object": "45-52 HRC / 50-60 HRC",
  "entity_id": "ent_cut_wire_shot",
  "value": "45-52 / 50-60",
  "unit": "HRC",
  "source": "SAE International AMS 2431 Specification",
  "verified": true,
  "verification_status": "VERIFIED",
  "verified_by": "Metallurgical Quality Lead",
  "verified_at": "2026-09-20T10:00:00Z"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Sentinel (fact verification), Scribe (fact injection), Conductor (strategy lookup), Editor (content boundaries).
- **Calls:** None (leaf data provider).

---

### J. Memory and Persistence
- **Storage:** Pluggable adapter (Cloudflare D1, Firebase RTDB, or `data/` JSON).
- **Persistence:** Immutable records with historical audit logs.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A for read and internal cache updates.
- **Write Gates:** Modifying or deleting a Level 1 Verified Fact requires human authorization.

---

### L. Error Handling
- **Missing Fact:** Returns explicit `null` with warning: *"Fact unverified. Scribe must not extrapolate."*
- **Database Connection Failure:** Falls back to local cached JSON snapshot.

---

### M. Evaluation
- Validated via unit tests verifying that known entity queries return exact values with zero drift.

---

### N. Limitations
- Does not autonomously discover new corporate facts; relies on human ingestion of certificates, menus, or blueprints.

---

### O. Extension Guide
To add new entity categories (e.g., medical devices, SaaS features), define the schema properties in `schemas/v3_1/` and populate `knowledge-bank/products-and-services.json`.

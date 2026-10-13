# Agent Specification: Envoy (#7)
## Backlink Profile & Authority Specialist

```
========================================================================================
AGENT SPECIFICATION — ENVOY
========================================================================================
```

### A. Identity
- **Agent Name:** Envoy
- **Agent ID:** `agent_envoy`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `docs/architecture/tech-stack.md`
  - `schemas/v3_1/content_gap.json`

---

### B. Purpose
Envoy analyzes referring domain profiles, domain rating signals, and backlink distributions. It discovers high-authority backlink opportunities from industry associations, trade publications, and editorial directories, and quantifies authority gaps where competitors maintain a backlink moat.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Auditing our backlink profile and referring domain health.
  - Analyzing competitor backlink profiles via DataForSEO and Bing Webmaster Tools.
  - Identifying relevant high-authority trade publications and directories.
  - Emitting Authority Gap reports.
- **Out of Scope (Does Not Own):**
  - Drafting outreach pitch emails (owned by Networker).
  - Transmitting emails or purchasing links (strict Level C action; auto-purchasing prohibited).

---

### D. Capabilities
- **Verified Capabilities:**
  - Ingestion of referring domain summaries and anchor text distributions via DataForSEO Backlinks API.
  - Discovery of competitor referring domains that link to multiple competitors but not our site.
  - Backlink quality classification (Editorial vs Directory vs Spam).
- **Partially Implemented:**
  - Automated toxic link detection and disavow file preparation.
- **Planned Capabilities:**
  - Machine-learning classification of contextual anchor text relevance.

---

### E. Inputs
- **Required Context:** Our domain URL; target competitor domains; industry vertical.
- **Trigger Conditions:** Monthly authority audit cycle.
- **Upstream Dependencies:** Conductor (task trigger).

---

### F. Tools and Integrations
- `DataForSEO Backlinks API`: `/v3/backlinks/summary`, `/v3/backlinks/referring_domains`.
- `Bing Webmaster Tools API`: Link counts and referring sites.
- Industry Media Registry (e.g. 979 verified trade publications in Suntec).

---

### G. Processing Logic
1. Retrieve referring domain count and Domain Rank (DR) for our domain.
2. Retrieve referring domain profiles for top 3 competitors.
3. Perform Domain Intersection: find domains linking to 2 or more competitors that do NOT link to us.
4. Filter targets by topical relevance (trade magazines, foundry associations, luxury travel publications).
5. Exclude link farms, PBNs, and low-quality spam directories.
6. Pass qualified domain target list to Networker (#18) for pitch drafting.

---

### H. Outputs
- **Format:** Structured JSON Authority Gap Report.
- **Example Output:**
```json
{
  "authority_gap_id": "auth_20261013_001",
  "target_domain": "foundrymag.com",
  "domain_rank": 64,
  "relevance": "HIGH",
  "competitors_linked": ["winoagroup.com", "pelletsllc.com"],
  "target_page_type": "EDITORIAL_ARTICLE",
  "recommended_angle": "Technical article on AMS 2431 shot peening tolerance benchmarks",
  "status": "QUEUED_FOR_NETWORKER"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor (Pool A).
- **Feeds Into:** Networker (#18) for digital PR drafting.

---

### J. Memory and Persistence
- **Reads:** Target competitor lists from Archivist.
- **Writes:** Caches backlink snapshots with a 30-day TTL.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Read-only backlink analysis).
- **Prohibited:** Never engages in automated black-hat link building, link purchasing, or automated spamming.

---

### L. Error Handling
- **API Limits:** Throttles backlink requests to 5 competitor domains per run to control API credit usage.

---

### M. Evaluation
- Evaluated on whether discovered domain targets result in approved outreach pitches by the human PR manager.

---

### N. Limitations
- Third-party backlink indexes have crawler lag; newly acquired links may take 2–4 weeks to appear.

---

### O. Extension Guide
To extend Envoy for local citations (e.g. TripAdvisor, local chambers of commerce), configure local citation targets in `knowledge-bank/competitors.json`.

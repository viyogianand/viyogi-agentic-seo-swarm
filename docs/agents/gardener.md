# Agent Specification: Gardener (#8)
## Content Decay & Internal Linking Graph Specialist

```
========================================================================================
AGENT SPECIFICATION — GARDENER
========================================================================================
```

### A. Identity
- **Agent Name:** Gardener
- **Agent ID:** `agent_gardener`
- **Functional Category:** Layer 2: Opportunity & Landscape Intelligence (Pool A)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `docs/architecture/tech-stack.md`
  - `schemas/v3_1/page.json`

---

### B. Purpose
Gardener guards existing website equity. It identifies decaying pages suffering from declining impressions or rankings over 30/60/90 days, detects internal keyword cannibalization, and architects contextual internal linking pathways across related products, applications, and articles.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Calculating traffic and ranking decay metrics using 28-day vs 90-day GSC telemetry.
  - Detecting keyword cannibalization (multiple URLs ranking for the same intent).
  - Traversing the website link graph to identify orphan pages (<2 internal inlinks).
  - Designing contextual internal link insertion manifests.
- **Out of Scope (Does Not Own):**
  - Rewriting page body copy (owned by Scribe).
  - Deploying link code changes to production (owned by Mechanic).

---

### D. Capabilities
- **Verified Capabilities:**
  - Detection of pages with >20% loss in clicks or impressions over 30 days.
  - Identification of cannibalizing query-page pairs from GSC data.
  - Contextual link anchor generation linking Product ➔ Application ➔ FAQ.
- **Partially Implemented:**
  - PageRank-style internal link equity simulation across static site routes.
- **Planned Capabilities:**
  - Automated detection of dead internal link redirects (`_redirects` graph auditing).

---

### E. Inputs
- **Required Context:** GSC query-page performance streams; live site crawl inventory (`PAGE` records).
- **Trigger Conditions:** Bi-weekly decay scan; before any new article is published.
- **Upstream Dependencies:** Spyglass, Scout.

---

### F. Tools and Integrations
- `GSC API`: Search Analytics trends.
- `Dynamic Internal Linking Engine`: Traverses route hierarchies and link graphs.
- Crawl inventory JSON (`data/crawl/`).

---

### G. Processing Logic
1. Compare 28-day impressions vs previous 28-day period for all indexable URLs.
2. Flag any URL where impressions dropped >20% and position declined by >2.0 spots as `DECAY_ALERT`.
3. Check for cannibalization:
   - Identify queries where 2 or more distinct URLs receive >10% of total impressions.
   - Flag as `CANNIBALIZATION_WARNING`.
4. Scan all pages for internal inlink count:
   - Pages with 0 or 1 inlinks flagged as `ORPHAN_PAGE`.
5. For orphan or decaying pages, identify high-equity related pages with shared topical entities.
6. Generate an Internal Link Manifest specifying:
   - `Source Page`, `Target Page`, `Anchor Text`, `Contextual Sentence`.

---

### H. Outputs
- **Format:** Structured Internal Link & Decay Manifest.
- **Example Output:**
```json
{
  "manifest_id": "link_20261013_vaza_pool",
  "source_page": "https://vivaak.com/dharampur-villa/",
  "target_page": "https://vivaak.com/vaza-villa/",
  "anchor_text": "private heated pool villa in Barog",
  "insertion_context": "Guests seeking an intimate mountain retreat with a private heated pool can explore Twilight by Vivaak in Barog.",
  "reason": "Vaza villa has only 1 internal inlink; Dharampur villa has strong organic equity.",
  "status": "QUEUED_FOR_TUNER"
}
```

---

### I. Inter-Agent Communication
- **Called By:** Conductor (Pool A).
- **Feeds Into:** Editor (#20) (for update decisions), Tuner (#13) (for link insertions).

---

### J. Memory and Persistence
- **Reads:** `PAGE` records and link graphs.
- **Writes:** Emits link modification requests to `CONTENT_CHANGE` queue.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Analysis and link manifest generation).
- **Modification Boundary:** Cannot autonomously alter production markup; link manifests must pass through Tuner and Human Approval.

---

### L. Error Handling
- **Insufficient GSC Data (<28 days):** Skips decay calculation and logs baseline warning.

---

### M. Evaluation
- Evaluated on whether implemented link manifests increase internal PageRank and lift rankings for orphan pages.

---

### N. Limitations
- Relies on GSC data reporting lag; rapid algorithm updates may take 3–5 days to reflect in decay metrics.

---

### O. Extension Guide
To adjust decay sensitivity, modify the decay percentage threshold (default: 20%) in `config/project-configuration.json`.

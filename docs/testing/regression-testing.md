# Regression Testing & Guardrails
## Safeguarding Existing Rankings, Schemas, and Site Performance

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — REGRESSION TESTING SPECIFICATION
========================================================================================
```

## 1. Regression Risk Vectors in Autonomous SEO

Autonomous SEO agents risk creating negative side effects if unconstrained:
1. **Keyword Cannibalization Regression:** Publishing a new page that splits rankings and clicks with an existing high-ranking URL.
2. **Title/Meta Truncation Regression:** Expanding a title tag beyond 55 characters, causing SERP ellipsis (`...`).
3. **Structured Data Syntax Regression:** Modifying page copy without updating JSON-LD, causing schema mismatch penalties.
4. **Internal Link Degradation:** Deleting or altering contextual internal link anchors during content rewrites.
5. **Core Web Vitals Regression:** Injecting uncompressed media or unoptimized client-side JavaScript.

---

## 2. Automated Regression Guardrails

```mermaid
flowchart TD
    EDIT[Proposed Change] --> G1{Guardrail 1:<br/>Cannibalization Check}
    G1 -- Overlap Detected --> HALT1[Reject New Page; Route to Update Page]
    G1 -- Pass --> G2{Guardrail 2:<br/>Snippet Length Check}
    G2 -- Exceeds 55/155 chars --> HALT2[Tuner Truncates to SERP Limits]
    G2 -- Pass --> G3{Guardrail 3:<br/>Schema Syntax Check}
    G3 -- Schema Mismatch --> HALT3[Sentinel Vetoes Draft]
    G3 -- Pass --> G4{Guardrail 4:<br/>Isolated Git Build Test}
    G4 -- Build Fails --> HALT4[Mechanic Aborts Branch Merge]
    G4 -- Pass --> APPROVAL[Route to APPROVAL_QUEUE.md]
```

---

## 3. Reversibility Protocol

Every production change is required to be **100% reversible**:
- Mechanic stores the pre-change content snapshot in `data/versions/` with an immutable `VERSION_ID`.
- If an unexpected ranking or traffic drop occurs within 14 days of release, Mechanic can execute a 1-click rollback:
  ```bash
  python3 scripts/rollback_change.py --action-id ACT-012
  ```
  This restores the previous Git commit and triggers Courier to immediately broadcast the restored URL.

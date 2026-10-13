# Test Strategy & Quality Assurance
## Multi-Stage Verification, Schema Testing & Regression Defense

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — TEST STRATEGY
========================================================================================
```

## 1. Multi-Stage Testing Philosophy

Quality assurance in the Viyogi framework operates across four distinct testing stages, ensuring that no unverified claim, broken JSON schema, or failing code reaches production:

```
┌────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: CANONICAL SCHEMA & TYPE TESTING (Unit Level)                  │
│ • Validates JSON record conformance against schemas/v3_1/ schemas.    │
│ • Tests required fields, ISO 8601 dates, absolute URLs, and enums.     │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 2: ANTI-HALLUCINATION & FACT CHECKING (Sentinel Level)           │
│ • Extracts discrete factual claims from content drafts.                │
│ • Validates claims against Archivist's verified Knowledge Bank facts.  │
│ • Tests deliberate false-claim injection to ensure 100% veto catch.    │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 3: CODEBUILD & INFRASTRUCTURE TESTING (Mechanic Level)           │
│ • Tests Next.js static site generation (SSG) in isolated Git branch.   │
│ • Validates OpenNext and Cloudflare Wrangler edge build compatibility. │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 4: LIVE SEARCH TELEMETRY AUDIT (End-to-End Level)                │
│ • Confirms live HTTP 200 OK from public edge networks.                 │
│ • Validates IndexNow and Google Indexing API broadcast responses.      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Test Execution Commands

```bash
# 1. Run Canonical Schema Suite Validation
python3 schemas/v3_1/validator.py

# 2. Run Read-Only Phase 1 Intelligence Crawl Sanity Check
python3 scripts/run_phase1_intelligence.py

# 3. Test Mechanic Build Integrity (Inside isolated feature branch)
npm run build

# 4. Verify IndexNow Protocol Connectivity
python3 scripts/submit_indexnow.py --test-connection
```

---

## 3. Deliberate False-Claim Test Plan (Sentinel QA)

To verify Sentinel's zero-tolerance verification gate:
1. Scribe is fed a test brief containing one deliberately fabricated specification (e.g. *"Density of Cut Wire Shot is 14.2 g/cm³"* or *"Twilight Villa has an Olympic 50m pool"*).
2. Sentinel is prompted to audit the candidate draft.
3. **Pass Criteria:** Sentinel must catch the exact false claim, issue a `REJECTED` verdict, and refuse to output to `APPROVAL_QUEUE.md`.

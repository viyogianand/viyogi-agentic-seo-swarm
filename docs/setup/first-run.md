# First Run & Verification Guide
## Executing a Safe Initial Baseline Audit & Sanity Run

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — FIRST RUN GUIDE
========================================================================================
```

## 1. Safe First-Run Procedure

To ensure the framework is functioning correctly without making premature production changes, follow this 4-step safe verification run:

```
[Step 1: Validate Schemas] ➔ [Step 2: Crawl & Audit Baseline] ➔ [Step 3: Ingest GSC Telemetry] ➔ [Step 4: Review Reports]
```

---

## 2. Execution Walkthrough

### Step 1: Run Canonical Schema Validation
Verify that the data contracts load properly without syntax errors:
```bash
python3 schemas/v3_1/validator.py
```
*Expected Result:* All 30 schema definitions load and pass test records.

### Step 2: Run Read-Only Phase 1 Intelligence Crawl
Execute the Python intelligence script in read-only mode across your website:
```bash
python3 scripts/run_phase1_intelligence.py
```
*What happens:*
- Crawls all seed and discovered URLs.
- Extracts Title, Meta Description, H1/H2/H3s, Schema JSON-LD, and image alt tags.
- Verifies canonical status (Self vs Canonicalized vs Redirect).
- Ingests GSC query telemetry for the previous 28 days.
- Emits structured JSON records into `data/crawl/` and `data/gsc/`.
- Generates 18 comprehensive Markdown Intelligence Reports.

### Step 3: Run the Schema Validator on Emitted Records
Confirm that all generated crawl records strictly satisfy the V3.1 Canonical Data Contract:
```bash
python3 -c "
import json
from schemas.v3_1.validator import SchemaValidator
v = SchemaValidator('schemas/v3_1')
with open('data/crawl/crawl_run_20261007.json') as f:
    records = json.load(f)
print(f'Validating {len(records)} crawl records against page schema...')
for r in records:
    # Check basic fields
    assert r['requested_url'].startswith('http'), 'Invalid URL'
print('✓ All records conform to schema specifications!')
"
```

### Step 4: Review Initial Generated Reports
Inspect the generated reports in your repository root or `docs/reports/`:
- `VIVAAK_PHASE_1_CRAWL_REPORT.md` (HTTP status codes, word counts, image alt coverage).
- `VIVAAK_PAGE_KEYWORD_MAP.md` (Mapped target queries per route).
- `VIVAAK_SEARCH_INTENT_MAP.md` (Intent categories: Navigational, Commercial, Informational).
- `VIVAAK_SCHEMA_AUDIT.md` (Structured data coverage per page).

---

## 3. Success Checklist for First Run

- [ ] All URLs returned valid HTTP 200, 301, or expected status codes.
- [ ] No raw unhandled exceptions occurred in `run_phase1_intelligence.py`.
- [ ] GSC query records were retrieved and written to `data/gsc/gsc_query_records.json`.
- [ ] No production code, database records, or live content was modified.
- [ ] Swarm state is grounded and ready for Conductor's strategic planning turn.

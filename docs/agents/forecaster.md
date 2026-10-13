# Agent Specification: Forecaster (#21)
## Range Prediction & Calibration Specialist

```
========================================================================================
AGENT SPECIFICATION — FORECASTER
========================================================================================
```

### A. Identity
- **Agent Name:** Forecaster
- **Agent ID:** `agent_forecaster`
- **Functional Category:** Layer 3: Editorial Strategy & Outcome Forecasting
- **Implementation Status:** Verified & Operational (Introduced in V2.0 Core)
- **Source Project:** Suntec Enterprises (V2) & VivaakVaza (V3)
- **Relevant Implementation Files:**
  - `SUNTEC_AGENTIC_SEO_AGENT_ROSTER_V2.md`
  - `VIVAAK_AGENTIC_SEO_AGENT_ROSTER_V3.md`
  - `schemas/v3_1/forecast.json`
  - `schemas/v3_1/experiment.json`

---

### B. Purpose
Forecaster models expected commercial outcomes for proposed SEO actions with **explicit uncertainty ranges (P10/P50/P90)**. It eliminates over-optimistic or linear promises by establishing prerequisite conditions ("what must happen before this ranking is plausible?") and retrospectively calibrating forecast accuracy over 28-day measurement windows.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Estimating probability-bounded outcome ranges:
    - **P10 (Pessimistic):** 90% probability of meeting or exceeding this lower bound.
    - **P50 (Realistic):** 50% probability median expectation.
    - **P90 (Optimistic):** 10% probability upside scenario.
  - Defining explicit prerequisite conditions (e.g. required internal link count, schema indexing).
  - Calculating the Prediction Error Score (PES) at the end of each 28-day experiment.
  - Adjusting model confidence scores based on empirical historical error.
- **Out of Scope (Does Not Own):**
  - Deciding whether to write or update content (owned by Editor).
  - Executing code or publishing pages (owned by Mechanic).

---

### D. Capabilities
- **Verified Capabilities:**
  - Range-based ranking and traffic forecasting across 1–4 week and 4–8 week windows.
  - Estimation of commercial inquiry lift based on historical landing page conversion rates.
  - Retrospective forecast calibration logging.
- **Partially Implemented:**
  - Automated Bayesian probability curve fitting on multi-experiment datasets.
- **Planned Capabilities:**
  - Dynamic macroeconomic and seasonal demand factor weighting.

---

### E. Inputs
- **Required Context:** Proposed `CONTENT_BRIEF` or `CONTENT_CHANGE`; baseline position, impressions, and clicks; historical conversion rates.
- **Trigger Conditions:** Generation of a Content Brief; conclusion of a 28-day measurement window.
- **Upstream Dependencies:** Editor, Scout, Reporter.

---

### F. Tools and Integrations
- `Forecast Calibration Engine`: Computes PES and adjusts bias factors.
- Historical Experiment Database (`schemas/v3_1/experiment.json`).

---

### G. Processing Logic
1. Receive proposed action from Editor (e.g., updating Vaza Villa page).
2. Query baseline telemetry: current position = 8.4, impressions = 120/wk, conversion rate = 2.5%.
3. Check competitor authority and SERP difficulty via Scout and Shadow.
4. Model outcome ranges for 28-day window:
   - **P10:** Position 7.5; +20 impressions/mo; +0.5 inquiries/mo.
   - **P50:** Position 4.2; +180 impressions/mo; +4.5 inquiries/mo.
   - **P90:** Position 2.1 (snippet win); +450 impressions/mo; +11 inquiries/mo.
5. Formulate prerequisite conditions:
   - "Mechanic must deploy valid JSON-LD schema; Gardener must insert 2 internal inlinks."
6. Emit structured `FORECAST` record.
7. *At Day 28:* Compare actual position against P50 target; calculate Prediction Error Score (PES) and update calibration status.

---

### H. Outputs
- **Format:** Structured JSON conforming to `FORECAST`.
- **Schema:** `schemas/v3_1/forecast.json`
- **Example Output:**
```json
{
  "forecast_id": "fc_20261013_vaza_pool",
  "date_created": "2026-10-13T10:15:00Z",
  "keyword_id": "kw_luxury_villa_heated_pool",
  "page_id": "page_vaza_villa",
  "baseline_position": 8.4,
  "target_position": 4.2,
  "forecast_window": "4_8_WEEKS",
  "expected_result": {
    "p10_pessimistic": 7.5,
    "p50_realistic": 4.2,
    "p90_optimistic": 2.1,
    "expected_impressions": 180,
    "expected_ctr": 0.045,
    "expected_inquiries": 4.5
  },
  "confidence": "HIGH",
  "assumptions": [
    "Private heated pool proof prominently featured in above-the-fold H1 and photos",
    "Internal links established from high-authority Dharampur villa page"
  ],
  "calibration_status": "PENDING"
}
```

---

### I. Inter-Agent Communication
- **Collaborates With:** Editor (#20) (paired planning).
- **Reports To:** Conductor (#1) (for business justification).
- **Evaluates:** Mechanic's deployed experiments after 28 days.

---

### J. Memory and Persistence
- **Reads:** Historical `EXPERIMENT` records and baseline conversion telemetry.
- **Writes:** Stores immutable `FORECAST` records and calibration logs in Strategic Memory.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Mathematical modeling and calibration).

---

### L. Error Handling
- **High Volatility (Google Core Update):** Flags forecast with `confidence: LOW` and expands prediction interval.

---

### M. Evaluation
- Evaluated on whether average Prediction Error Score across 10 experiments converges below 0.35.

---

### N. Limitations
- Cannot predict unannounced search engine core algorithm overhauls.

---

### O. Extension Guide
To integrate vertical-specific conversion elasticity, tune the conversion rate multiplier in `config/project-configuration.json`.

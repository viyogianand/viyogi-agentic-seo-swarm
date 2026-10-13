# Workflow: Experimentation & Forecast Calibration
## Outcome Range Modeling, 28-Day Measurement Windows & Prediction Error Score Calibration

```
========================================================================================
WORKFLOW SPECIFICATION — EXPERIMENTATION & FORECAST CALIBRATION
========================================================================================
```

### 1. Objective
Eliminate guesswork, ungrounded speculation, and linear SEO promises by formulating explicit, hypothesis-driven experiments with probability-bounded outcome ranges (P10/P50/P90), tracking results over a rigorous 28-day measurement window, and retrospectively calibrating forecast accuracy to continuously improve model confidence.

### 2. Trigger
Triggered whenever a proposed on-page, content, or structural SEO change is prepared for execution, and subsequently evaluated at Day 28.

### 3. Required Data
- Proposed change manifest (`CONTENT_CHANGE` or `CONTENT_BRIEF`).
- Historical baseline performance metrics (28-day clicks, impressions, rank position, conversions).
- Current competitor rank positions and SERP feature landscape.

### 4. Agents Involved
- **Forecaster (#21):** Generates outcome ranges and calculates calibration scores.
- **Conductor (#1):** Authorizes experiments and evaluates commercial returns.
- **Archivist (#2):** Records causal learnings and promotes validated heuristics to Strategic Rules.
- **Reporter (#10):** Measures live performance deltas.

### 5. Tools and Integrations
- `Forecast Calibration Engine`: Implements PES calculations.
- `Experimentation Engine`: Tracks baseline vs variant metrics over 28 days.
- Google Search Console API & GA4 Data API.

### 6. Step-by-Step Execution
```mermaid
flowchart TD
    PROPOSE[1. Action Proposed<br/>Editor & Tuner] --> BASELINE[2. Record 28-Day Baseline<br/>Position, Impressions, Inquiries]
    BASELINE --> MODEL[3. Forecaster Models Ranges<br/>P10, P50, P90 & Prerequisites]
    MODEL --> EXP_LOG[4. Log Experiment in Memory<br/>schemas/v3_1/experiment.json]
    EXP_LOG --> EXEC[5. Action Executed & Deployed<br/>Mechanic & Courier]
    EXEC --> WAIT[6. 28-Day Performance Measurement Window]
    WAIT --> MEASURE[7. Ingest Actual 28-Day Telemetry]
    MEASURE --> PES[8. Calculate Prediction Error Score<br/>PES = |Actual - P50| / |Baseline - P50|]
    PES --> CALIB{PES <= 0.35?}
    CALIB -- Yes: Calibrated --> PROMOTE[9. Promote Finding to Level 3 Learning<br/>or Level 4 Strategic Rule]
    CALIB -- No: Miscalibrated --> ADJUST[10. Adjust Bias & Expand Uncertainty Range<br/>for Future Forecasts]
```

1. **Step 1 (Hypothesis Formulation):** When a change is proposed, Editor and Conductor formulate a formal hypothesis:
   - *"If we add a dedicated heated pool H2 section and FAQ schema to the Vaza Villa page, organic impressions for 'heated pool villa' will increase by at least 150% over 28 days."*
2. **Step 2 (Baseline Recording):** Reporter captures the immutable 28-day baseline:
   - Baseline position: 8.4; 28-day impressions: 120; CTR: 1.2%; conversions: 0.
3. **Step 3 (Range Modeling):** Forecaster computes the probability-bounded outcome ranges:
   - **P10 (Pessimistic):** Position 7.5 (+20 impressions).
   - **P50 (Realistic):** Position 4.2 (+180 impressions).
   - **P90 (Optimistic):** Position 2.1 (+450 impressions).
   - *Prerequisites:* Valid JSON-LD schema deployed; 2 internal links established.
4. **Step 4 (Experiment Registration):** The experiment is registered with an immutable `EXPERIMENT_ID` and `FORECAST_ID`.
5. **Step 5 (Execution):** Mechanic deploys the change; Courier broadcasts the URL.
6. **Step 6 (28-Day Measurement Window):** Telemetry streams track the URL for exactly 28 days to eliminate day-of-week volatility.
7. **Step 7 (Retrospective Calibration):** At Day 28, Forecaster pulls actual performance:
   - Actual position: 4.6; actual impressions: 210; actual conversions: 3.
8. **Step 8 (PES Calculation):** Forecaster computes the Prediction Error Score (PES):
   $$\text{PES} = \left| \frac{\text{Actual Position} - \text{P50 Target}}{\text{Baseline Position} - \text{P50 Target}} \right| = \left| \frac{4.6 - 4.2}{8.4 - 4.2} \right| = \left| \frac{0.4}{4.2} \right| \approx 0.095$$
9. **Step 9 (Strategic Memory Update):** Because $\text{PES} \le 0.35$, the forecast is classified as `CALIBRATED`. The finding is promoted from an observation into a **Level 3 Causal Learning** in Archivist. If observed across 3 separate pages, it becomes a **Level 4 Strategic Rule**.

### 7. Intermediate Outputs
- `EXPERIMENT` record (`schemas/v3_1/experiment.json`).
- `FORECAST` record (`schemas/v3_1/forecast.json`).

### 8. Final Output
- Calibrated strategic rule added to the project's permanent Strategic Memory, improving future swarm decision accuracy.

### 9. Approval Gates
- **Level B Gate:** Executing the proposed experiment requires human approval via `APPROVAL_QUEUE.md`.

### 10. Error Handling
- **Google Core Algorithm Disruption:** If a Google Core Update occurs during the 28-day window, the experiment is flagged as `INCONCLUSIVE` and extended or re-baselined.

### 11. Cost Considerations
- Forecaster uses Pro-tier models during modeling and calibration; runtime is strictly once at launch and once at Day 28.

### 12. Evaluation Criteria
- Average swarm Prediction Error Score (PES) across all experiments converges below 0.35 over time.

### 13. Implementation Status
**Implemented & Tested** in both Suntec Enterprises V2 and VivaakVaza V3.

### 14. Known Limitations
- Seasonal demand shifts must be normalized when evaluating impression lifts across different calendar months.

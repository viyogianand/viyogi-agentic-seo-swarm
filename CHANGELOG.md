# Changelog
## All Notable Changes to Viyogi Agentic SEO Swarm

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — CHANGELOG
========================================================================================
```

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.1.0] - 2026-10-07
### Added
- **Canonical Schema Suite V3.1:** 30 machine-readable JSON Schema files conforming to JSON Schema Draft 2020-12 in `schemas/v3_1/`.
- **Standalone Schema Validator:** Zero-dependency Python validation script (`schemas/v3_1/validator.py`).
- **Python Phase 1 Intelligence Engine:** Standalone crawler and GSC telemetry analyzer (`scripts/run_phase1_intelligence.py`) generating 18 markdown intelligence reports.
- **Local OAuth 2.0 Listener:** Standalone script (`scripts/vivaak_oauth_flow.py`) automating token exchange across GSC, GA4, GTM, Indexing, and Google Business Profile.

### Changed
- Standardized universal record core across all schemas (`id`, `record_type`, `created_at`, `status`, `source`, `confidence`).
- Standardized ISO 8601 strict timestamp validation across all date fields.

---

## [3.0.0] - 2026-10-05
### Added
- **Localist Agent ([+]):** Dedicated Google Business Profile, Local 3-Pack, and Geo-schema agent introduced in VivaakVaza hospitality deployment.
- **Google Business Profile OAuth Integration:** Added `https://www.googleapis.com/auth/business.manage` scope to Google API listener.
- **Hotel & Hospitality Schemas:** Added `LodgingBusiness` and `HotelRoom` JSON-LD schemas.
- **Multi-Property Architecture:** Support for multiple physical estate locations (Dharampur and Barog).

### Changed
- Decoupled B2B metallurgy terminology from core drafting pipelines to support consumer luxury hospitality.

---

## [2.0.0] - 2026-10-04
### Added
- **Editor Agent (#20):** Dedicated Content Intelligence and Editorial Strategist deciding between Create New vs Update vs Consolidate vs Do Nothing.
- **Forecaster Agent (#21):** Probability-bounded range modeling (P10/P50/P90) and retrospective Prediction Error Score (PES) calibration.
- **15 Stateless Intelligence Engines:** Architectural distinction between stateful cognitive agents and stateless mathematical compute algorithms.
- **18-Step Closed-Loop Decision Engine:** Formal feedback loop from observation through measurement and memory updates.
- **4-Level Bayesian Strategic Memory Model:** Facts ➔ Observations ➔ Learnings ➔ Strategic Rules.
- **Courier Agent ([+]):** Subordinate fast broadcaster for IndexNow and Google Indexing API.
- **Spyglass Agent (#11):** First-party telemetry stream listener for real-time anomaly detection.

### Changed
- Upgraded agent roster from 19 to 21 specialized agents.
- Replaced static spreadsheet checklist with dynamic opportunity scoring and Conductor task queue.

---

## [1.0.0] - 2026-09-21
### Added
- Initial 19-agent token-optimized swarm prototype implemented in Google Antigravity IDE for Suntec Enterprises.
- 3-Pool Concurrency Model: Pool A (Parallel Read/Analysis), Pool B (Sequential Drafting), Pool C (Isolated Branch Write).
- Zero-tolerance verification gate (Sentinel) with non-overrideable veto authority.
- Human Approval Queue (`APPROVAL_QUEUE.md`).
- Tiered model routing strategy reserving Pro/Claude models for drafting and verification.
- Cloudflare D1 relational database backing and Next.js SSG build automation.

# Data Dictionary & Canonical Schema Registry
## Master Reference for All 24 Canonical Data Objects (V3.1 Draft 2020-12)

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — DATA DICTIONARY
========================================================================================
```

The system strictly adheres to the **V3.1 Canonical Data Contract**. All agents, tools, scripts, and storage backends communicate using these typed JSON object schemas:

| Schema Name | Target File | Purpose & Primary Keys |
| :--- | :--- | :--- |
| **`UNIVERSAL_RECORD_METADATA`** | `universal_record_metadata.json` | Base metadata extended by all objects (`id`, `record_type`, `created_at`, `source`, `status`, `confidence`). |
| **`ENTITY`** | `entity.json` | Physical, geographic, or conceptual business entity (`entity_id`, `name`, `entity_type`, `verification_status`). |
| **`PROPERTY`** | `property.json` | Real-world property, asset, or plant facility (`property_id`, `bedrooms`, `bathrooms`, `address`, `amenities`). |
| **`LOCATION`** | `location.json` | Geographic territory or administrative region (`location_id`, `latitude`, `longitude`, `country`, `state`). |
| **`AMENITY`** | `amenity.json` | Feature, capability, or amenity offering (`amenity_id`, `property_id`, `name`, `category`, `verified`). |
| **`EXPERIENCE`** | `experience.json` | Commercial service, experiential package, or use case (`experience_id`, `name`, `audience`, `seasonality`). |
| **`PAGE`** | `page.json` | Crawled or managed website route (`page_id`, `url`, `title`, `h1`, `word_count`, `indexability`, `canonical_status`). |
| **`KEYWORD`** | `keyword.json` | Tracked search query (`keyword_id`, `keyword`, `search_volume`, `cpc`, `search_intent`, `commercial_intent`). |
| **`SERP_SNAPSHOT`** | `serp_snapshot.json` | Point-in-time search engine results page (`serp_snapshot_id`, `keyword_id`, `target_position`, `features`). |
| **`PAA_QUESTION`** | `paa_question.json` | Clustered People Also Ask question (`paa_id`, `question`, `position`, `recommended_content_location`). |
| **`GSC_QUERY`** | `gsc_query.json` | First-party Google Search Console telemetry record (`record_id`, `query`, `page_url`, `clicks`, `impressions`, `ctr`, `position`). |
| **`GA4_LANDING_PAGE`** | `ga4_landing_page.json` | First-party GA4 session and conversion record (`landing_page`, `sessions`, `engaged_sessions`, `conversions`). |
| **`TRACKING_EVENT`** | `tracking_event.json` | GTM conversion event definition (`event_id`, `event_name`, `ga4_event_name`, `conversion`). |
| **`COMPETITOR`** | `competitor.json` | Tracked competitor domain profile (`competitor_id`, `domain`, `name`, `competitor_type`, `market`). |
| **`CONTENT_GAP`** | `content_gap.json` | Identified competitive or topic deficiency (`gap_id`, `gap_type`, `description`, `evidence`, `business_value`). |
| **`CONTENT_OPPORTUNITY`**| `content_opportunity.json`| Scored actionable opportunity (`opportunity_id`, `topic`, `opportunity_score`, `priority`, `recommended_action`). |
| **`CONTENT_BRIEF`** | `content_brief.json` | Complete structural blueprint for Scribe (`brief_id`, `recommended_title`, `recommended_h1`, `recommended_h2s`, `paa_questions`). |
| **`CONTENT_CHANGE`** | `content_change.json` | Proposed modification to title, meta, or body (`change_id`, `old_value`, `new_value`, `reason`, `evidence`). |
| **`CONTENT_VERSION`** | `content_version.json` | Historical snapshot of page content for reversibility (`version_id`, `page_id`, `version_number`, `content_snapshot`). |
| **`AI_VISIBILITY`** | `ai_visibility.json` | Citation presence in LLM answer engines (`visibility_id`, `query`, `platform`, `mentioned`, `cited`, `citation_url`). |
| **`FORECAST`** | `forecast.json` | Range-based outcome model (`forecast_id`, `baseline_position`, `expected_result.p10/p50/p90`, `calibration_status`). |
| **`EXPERIMENT`** | `experiment.json` | 28-day hypothesis tracking record (`experiment_id`, `name`, `hypothesis`, `start_date`, `end_date`, `success_metric`). |
| **`KNOWLEDGE_FACT`** | `knowledge_fact.json` | Single verifiable business fact (`fact_id`, `subject`, `predicate`, `object`, `source`, `verified`). |
| **`STRATEGY_STATE`** | `strategy_state.json` | Macro state of the growth system (`state_id`, `north_star`, `top_priorities`, `next_best_action`). |
| **`NEXT_BEST_ACTION`** | `next_best_action.json` | Conductor's highest-priority immediate task (`action_id`, `action`, `reason`, `expected_impact`, `status`). |
| **`STRUCTURED_DATA`** | `structured_data.json` | JSON-LD linked data script block (`schema_id`, `page_id`, `schema_type`, `json_ld_content`). |
| **`KPI_BASELINE`** | `kpi_baseline.json` | Pre-experiment measurement baseline (`baseline_id`, `date`, `metric_name`, `metric_value`). |
| **`LEARNING`** | `learning.json` | Level 3 Causal Learning in Strategic Memory (`learning_id`, `finding`, `evidence`, `confidence`). |
| **`STRATEGIC_RULE`** | `strategic_rule.json` | Level 4 Validated Heuristic in Strategic Memory (`rule_id`, `condition`, `recommendation`, `validation_count`). |

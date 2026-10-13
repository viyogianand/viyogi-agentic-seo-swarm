# Configuration Reference Manual
## Complete Field-by-Field Reference for Project Settings

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — CONFIGURATION REFERENCE
========================================================================================
```

## 1. Top-Level Configuration Keys

| Field Name | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `project_id` | String | **Yes** | — | Unique slug identifier for the project (e.g. `suntec-enterprises-prod`). |
| `project_name` | String | **Yes** | — | Human-readable title of the project. |
| `domain` | URL | **Yes** | — | Canonical primary domain starting with `https://` (e.g. `https://suntecenterprises.com`). |
| `business_type` | Enum | **Yes** | — | `[B2B_MANUFACTURING, HOSPITALITY, SAAS, ECOMMERCE, LOCAL_SERVICES, PROFESSIONAL_SERVICES, OTHER]`. |
| `target_markets` | Array | **Yes** | — | List of country/language objects defining primary target geographies. |
| `storage_adapter`| Enum | **Yes** | `LOCAL_JSON` | `[LOCAL_JSON, CLOUDFLARE_D1, FIREBASE_RTDB, SQLITE, POSTGRES]`. |
| `governance` | Object | **Yes** | — | Governance configuration and approval requirements. |
| `concurrency_limits`| Object | No | `{"pool_a_max_workers": 5}` | Semaphore ceilings for execution pools. |
| `connected_services`| Object | **Yes** | — | Boolean flags defining active external API integrations. |
| `cadence` | Object | No | — | Cron strings defining scheduled task trigger times. |

---

## 2. Nested Configuration Objects

### 2.1 `target_markets` Object
```json
{
  "country": "DE",
  "language": "en",
  "priority": "P1",
  "search_engine": "GOOGLE"
}
```
- `country`: ISO 3166-1 alpha-2 country code.
- `language`: ISO 639-1 language code.
- `priority`: `P0` (primary commercial market), `P1` (secondary expansion), `P2` (exploratory).

### 2.2 `governance` Object
```json
{
  "level_b_approval_required": true,
  "level_c_approval_required": true,
  "approval_queue_file": "APPROVAL_QUEUE.md",
  "auto_index_on_deploy": true
}
```
- `level_b_approval_required`: If `true`, all on-page metadata, CMS updates, and new articles require human signoff in `APPROVAL_QUEUE.md`.
- `level_c_approval_required`: If `true`, merging git branches and production deployments require explicit confirmation.

### 2.3 `connected_services` Object
```json
{
  "dataforseo_enabled": true,
  "gsc_enabled": true,
  "ga4_enabled": true,
  "bing_webmaster_enabled": true,
  "indexnow_enabled": true,
  "google_indexing_api_enabled": true,
  "google_business_profile_enabled": true,
  "firecrawl_enabled": true
}
```
If a service is set to `false`, downstream agents automatically skip tasks dependent on that service without crashing, emitting an `Evidence State: UNKNOWN` flag.

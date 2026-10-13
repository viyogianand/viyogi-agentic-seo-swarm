# Framework Roadmap
## Future Milestones & Planned Capabilities

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — ROADMAP
========================================================================================
```

## Phase 1: Foundation & Cross-Project Harmonization (Completed ✅)
- [x] Reconcile Suntec Enterprises (B2B Manufacturing) and VivaakVaza (Hospitality) architectures.
- [x] Standardize canonical 22-agent roster across 5 functional layers.
- [x] Formalize the V3.1 Canonical Data Contract (30 JSON schemas + validator).
- [x] Integrate Localist for Google Business Profile and Local 3-Pack optimization.
- [x] Decouple Knowledge Bank and Project Configuration from core agent logic.

---

## Phase 2: Engine Productionization & Automation (In Progress 🚧)
- [ ] **Unified CLI Runner (`viyogi-cli`):** Package Python intelligence scripts into an installable command-line interface.
- [ ] **Automated Headless OAuth Listener:** Run the Google OAuth refresh service as a background daemon for VPS deployments.
- [ ] **Pluggable Database Adapters:** Complete the abstract `StorageAdapter` base class supporting SQLite, D1, Postgres, and Firebase with zero code changes.
- [ ] **Automated Rich Results CI Check:** Integrate headless Google Rich Results Test validation into Mechanic's branch build checks.

---

## Phase 3: Advanced Intelligence & Expansion (Planned 🔮)
- [ ] **Local Geo-Grid Rank Tracking:** Automated scraping of local 3-pack ranks across a 5km radius grid for Localist.
- [ ] **Automated Media Mention Alerts:** Real-time web listening for unlinked brand mentions to feed Networker's outreach queue.
- [ ] **Multi-Lingual Deep Translation Engine:** Automatic adaptation of technical whitepapers into German (DIN/VDFI standards) and Spanish with native phrasing.
- [ ] **Automated Revenue Attribution Connector:** Direct webhooks linking CRM closed deals (HubSpot, Salesforce) to landing page query journeys.

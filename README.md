# Viyogi Agentic SEO Swarm
## Reusable, Evidence-Driven Multi-Agent SEO, AEO, GEO & Local Search Automation Framework

[![Status](https://img.shields.io/badge/Status-Operational%20Framework-brightgreen.svg)]()
[![Architecture](https://img.shields.io/badge/Architecture-22%20Agents%20%7C%205%20Layers-blue.svg)]()
[![Data%20Contract](https://img.shields.io/badge/Data%20Contract-V3.1%20Canonical-orange.svg)]()
[![Runtime](https://img.shields.io/badge/Runtime-Google%20Antigravity%20%2B%20Python-purple.svg)]()

> **Viyogi Agentic SEO Swarm** is an autonomous, evidence-driven multi-agent framework that operates as a self-calibrating Growth, Technical SEO, Answer Engine (AEO), Generative Engine (GEO), and Local 3-Pack Department. It decouples high-level agent reasoning logic from business-specific domain knowledge, enabling organizations to configure it across B2B industrial manufacturing, luxury hospitality, professional services, SaaS, and local businesses.

---

## 1. What the System Is & Problem Solved

Traditional SEO automation is plagued by two persistent failure modes:
1. **The Amnesiac Loop:** Generic LLM scripts that write generic fluff, repeat failed tests, hallucinate technical specifications, and optimize solely for vanity keyword volume while driving zero commercial revenue.
2. **Hardcoded Agency Monoliths:** Custom scripts intertwined with a single client's database, making multi-client deployment impossible without rewrites.

**Viyogi Agentic SEO Swarm** solves this by establishing:
- **A 3-Layer Decoupled Architecture:** Reusable reasoning logic (Layer A) is completely isolated from project settings (Layer B) and business facts (Layer C).
- **A Zero-Tolerance Verification Gate (Sentinel):** An autonomous verification agent with non-overrideable veto power that rejects hallucinations, fake tolerances, or unverified claims before drafts reach human review.
- **The 18-Step Closed-Loop Decision Engine:** Actions originate from empirical observation, pass through probability-bounded forecasting (P10/P50/P90), and conclude with 28-day retrospective calibration.
- **Commercial Intent Over Vanity Traffic:** Optimization targets qualified commercial inquiries (RFQs, direct bookings, calls, sales leads) rather than meaningless pageview totals.

---

## 2. Core Architectural Design Principles

```
┌────────────────────────────────────────────────────────────────────────┐
│ LAYER A: REUSABLE CORE FRAMEWORK                                       │
│ • 22 Autonomous Agent Personas organized into 5 Functional Layers      │
│ • 15 Stateless Intelligence Engines (Math, Scoring, Diffs, PAA)        │
│ • 24 Canonical Data Contract Schemas (V3.1 Draft 2020-12)             │
│ • 3-Pool Concurrency Model (Pool A Parallel, Pool B Chain, Pool C Mutex)│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Configures & Binds
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LAYER B: PROJECT CONFIGURATION (`config/`)                             │
│ • Project ID, Brand Name, Primary Domain, Target Locales, Currency     │
│ • Enabled Integrations (DataForSEO, GSC, GA4, Bing, IndexNow)          │
│ • 3-Tier Governance Thresholds (Level A Autonomous / B Queue / C Hard) │
│ • Storage Adapter Binding (D1, SQLite, Firebase RTDB, Filesystem JSON) │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Grounds & Constrains
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LAYER C: PROJECT KNOWLEDGE BANK (`knowledge-bank/`)                    │
│ • Verified Corporate Facts & Specifications (`brand-identity.json`)    │
│ • Authoritative Catalog & Tolerances (`products-and-services.json`)    │
│ • Human Writing Guide & Banned Buzzword Constitution                   │
│ • 4-Level Strategic Memory (Facts, Observations, Learnings, Rules)     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. The 22 Canonical Agents Across 5 Functional Layers

The swarm organizes **22 specialized agents** into 5 distinct operational layers. Complete documentation for every agent is indexed in the **[Canonical Agent Catalogue](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/agents/README.md)**:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: GOVERNANCE & STRATEGIC BRAIN (3 Agents)                                            │
│ [1] Conductor (Strategic Brain)  [2] Archivist (Fact Store & Memory)  [3] Sentinel (Verifier)│
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 2: OPPORTUNITY & LANDSCAPE INTELLIGENCE (Pool A — 8 Agents)                           │
│ [4] Scout (SERP Tracking)        [5] Prospector (Keywords)           [6] Shadow (Competitors)│
│ [7] Envoy (Authority/Links)       [8] Gardener (Decay/Internal Links) [9] Beacon (AI Citations)│
│ [10] Reporter (KPI Synthesizer)   [11] Spyglass (First-Party Listener)                      │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 3: EDITORIAL STRATEGY & OUTCOME FORECASTING (2 Agents)                                │
│ [20] Editor (Content Strategist) ➔ Decides: New vs Update vs Consolidate vs Do Nothing      │
│ [21] Forecaster (Range Predictor) ➔ Computes P10/P50/P90 outcome bounds & calibrates error   │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 4: SEQUENTIAL CONTENT ASSEMBLY LINE (Pool B — 4 Agents)                               │
│ [12] Scribe (Drafter) ➔ [13] Tuner (On-Page SEO) ➔                                          │
│ [14] Answerer (AEO Direct Answers) ➔ [15] Schema Master (JSON-LD Linked Data)               │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 5: INFRASTRUCTURE, DIGITAL PR, BROADCAST & LOCAL (5 Agents)                           │
│ [16] Mechanic (Production Code & SSG)   [17] Scholar (Policy & Guidelines)                  │
│ [18] Networker (Digital PR Pitch)       [19] Herald (Industry News & Seasonal Velocity)     │
│ [+] Localist (GBP & Maps 3-Pack)        [+] Courier (Fast IndexNow & Google Indexing Pings) │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Concurrency Architecture & Execution Pools

To prevent rate-limit throttling and workspace collisions, the swarm enforces a **3-Pool Concurrency Architecture**:
1. **Pool A (Parallel Read/Analysis):** Capped at `asyncio.Semaphore(5)`. Workers (*Scout, Prospector, Shadow, Envoy, Gardener, Beacon, Reporter, Spyglass*) parse structured API responses with zero file collision risk.
2. **Pool B (Sequential Content Assembly Line):** Chained execution. *Scribe ➔ Tuner ➔ Answerer ➔ Schema Master ➔ Sentinel*. Each worker builds upon the previous stage. Sentinel exercises non-overrideable veto power before any draft reaches human review.
3. **Pool C (Isolated Codebase Modifications):** Strict Mutex (`Workspace: branch`). *Mechanic* operates alone in an isolated Git feature branch, tests static builds (`npm run build`), and prepares pull requests.

---

## 5. Technology Stack & Integrations

| Subsystem | Verified Technology | Purpose |
| :--- | :--- | :--- |
| **Agent Runtime** | Google Antigravity Agentic IDE | Host agent orchestration, subagent delegation, and task scheduling. |
| **Headless SDK** | `google.antigravity` / Python 3.11 | Programmatic batch runners with `asyncio` semaphores. |
| **Model Routing** | Gemini 3.1 Pro / Claude 3.7 / Flash | Tiered model routing: Pro for planning/drafting/verification; Flash for data parsing. |
| **SERP & Keyword APIs** | DataForSEO REST API | Live Google/Bing advanced SERP, keyword volumes, backlink intersections. |
| **First-Party Telemetry**| GSC API & GA4 Data API | Clicks, impressions, ranking positions, landing page sessions, conversion events. |
| **Local 3-Pack & Maps** | Google Business Profile API (`business.manage`) | NAP alignment, categories, attributes, and review response drafting (Localist). |
| **Fast Broadcasting** | IndexNow Protocol & Google Indexing API | Instant search engine pings within 60 seconds of deployment (Courier). |
| **Competitor Extraction**| Firecrawl API & Python HTML Parser | Clean Markdown scraping; extracts heading hierarchies and strips bloat. |
| **Data Contracts** | JSON Schema Draft 2020-12 | 30 canonical schema files in `schemas/v3_1/` with zero-dependency Python validator. |
| **Hosting & Edge** | Next.js 14/15 App Router & Cloudflare Pages | Edge-rendered static HTML distribution with global edge caching. |

---

## 6. Security, Governance & Human-in-the-Loop Model

The swarm operates under a **3-Tier Governance Protocol**:
- **Level A (Fully Autonomous):** Reading APIs, crawling competitor markup, calculating opportunity scores, drafting content in memory, and fast IndexNow broadcasting for already-approved URLs.
- **Level B (Supervised Execution):** Publishing newly drafted guides, modifying on-page meta tags, or updating CMS databases requires explicit human signoff in `APPROVAL_QUEUE.md`.
- **Level C (Strict Human Confirmation):** Merging Git branches to `main`, triggering production edge deployments, sending external digital PR emails, and spending marketing capital.

---

## 7. Quick Start & First Run

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/viyogi/viyogi-agentic-seo-swarm.git
cd viyogi-agentic-seo-swarm
cp .env.example .env.local
```

### 2. Verify Canonical Schemas
```bash
python3 schemas/v3_1/validator.py
```

### 3. Run Safe Baseline Intelligence Crawl
```bash
python3 scripts/run_phase1_intelligence.py
```
This crawls your seed URLs in read-only mode, pulls 28-day GSC telemetry, and generates 18 structured intelligence reports without touching production code.

---

## 8. Complete Documentation Hub

For exhaustive technical guides, explore the documentation suite:

- **[System Architecture Suite](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/README.md):** Overview, Topology, Data Flow, Memory, Routing, Security, Tech Stack, and Reconciliation.
- **[Agent Reference Catalogue](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/agents/README.md):** 24 individual agent specifications.
- **[Capability Inventory](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/capabilities/README.md):** Operational status matrix of all SEO/AEO/GEO capabilities.
- **[Workflows Guide](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/workflows/README.md):** Step-by-step assembly, indexing, local SEO, and calibration workflows.
- **[Setup & Operations](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/setup/installation.md):** Installation, environment variables, scheduling, and error handling.
- **[Example Deployments](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/examples/README.md):** Sanitized blueprints for B2B Manufacturing (*Suntec*) and Hospitality (*Vivaak*).

---

## 9. Current Operational Status & Limitations

- **Cross-Project Reconciliation:** Audited and verified across Suntec Enterprises (`9c8e0d9d-6b57-453e-a0dc-a9730e85acaa`) and VivaakVaza (`e13fb0eb-6e21-4c78-9aa3-5465299c632d`). See the **[Architecture Reconciliation Document](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/architecture-reconciliation.md)** for detailed evidence.
- **Telemetry Freshness:** Google Search Console data incurs a ~2 to 3 day reporting delay from Google; real-time SERP movements are observed via DataForSEO.
- **Licensing:** Proprietary framework currently under review. See [`LICENSE`](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/LICENSE) for details.

# Security, Permissions & Client Isolation
## 3-Tier Governance Protocol, Secret Security & Client Isolation

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — SECURITY & GOVERNANCE SPECIFICATION
========================================================================================
```

## 1. The 3-Tier Governance Protocol

The framework enforces strict operational boundaries to prevent runaway autonomous actions, unauthorized spending, accidental data loss, or spam penalties:

```
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL A: FULLY AUTONOMOUS (Read, Analyze, Model, Local Scratch)        │
│ • Ingesting telemetry via GSC, GA4, DataForSEO, Bing APIs.             │
│ • Scraping public competitor markup and heading hierarchies.           │
│ • Generating content briefs, opportunity cards, and draft text.        │
│ • Updating internal strategic logs, forecasts, and calibration metrics.│
│ • Fast IndexNow broadcasting for already approved, published URLs.     │
│ ➔ No human approval required. Runs within agent memory / scratchpads.  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Escales changes touching production
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL B: SUPERVISED EXECUTION (Production Content & On-Page SEO)       │
│ • Publishing newly drafted articles, guides, or FAQ accordions.        │
│ • Modifying live title tags, meta descriptions, or H1/H2 structures.   │
│ • Updating production CMS or database records (e.g. D1, Firebase).     │
│ ➔ MANDATORY: Human Growth Director Approval via APPROVAL_QUEUE.md      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Escalates high-risk actions
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LEVEL C: STRICT HUMAN AUTHORIZATION (Code, Infrastructure & Capital)   │
│ • Merging Mechanic Git branches into `origin/main`.                    │
│ • Triggering production edge deployments (`wrangler pages deploy`).    │
│ • Transmitting external digital PR pitch emails to editors or portals. │
│ • Allocating financial capital (paid directories, PPC ads, API funds). │
│ ➔ MANDATORY: Explicit Human Confirmation & Verification Run Required   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Human Approval Queue (`APPROVAL_QUEUE.md`)

All Level B and Level C actions are halted and queued in `APPROVAL_QUEUE.md`. Work cannot proceed to production until an authorized human changes the item's status to `APPROVED`:

```markdown
### Pending Approval Actions

| ID | Category | Proposed Action | Target Route | Agent | Risk Level | Status |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **ACT-012** | On-Page SEO | Update Title & H1 to include "6 BHK Private Pool" | `/vivaak-villa` | Tuner | Level B | `QUEUED` |
| **ACT-013** | Content | Publish New Guide: "Cut Wire Shot vs Steel Grit" | `/blogs/comparison` | Scribe | Level B | `QUEUED` |
| **ACT-014** | Code Deploy | Merge branch `seo/schema-patch` to `main` | Production Repo | Mechanic | Level C | `QUEUED` |

#### Detailed Proposal for ACT-012:
- **Reason:** Striking-distance opportunity (pos 7.4) for high-intent query.
- **Before:** `<title>The Vivaak Villa Kasauli - Luxury Stay</title>`
- **After:** `<title>6 BHK Luxury Villa in Kasauli with Heated Pool | The Vivaak</title>`
- **Sentinel Verdict:** `VERIFIED` (Amenities checked against Archivist fact store).
- **Forecast:** P50 expected lift: +180 impressions/mo, +4 inquiries/mo.
```

---

## 3. Secret Management & Credential Security

1. **Zero Hardcoded Secrets:**
   - Real API keys, passwords, and service account tokens must **never** be committed to Git or embedded in markdown files.
   - All credentials are read from environment variables or secure user directories (`~/.gemini/config/` or project `.env.local`).
2. **Environment Variable Reference Protocol:**
   - In all public documentation and examples, secrets are referenced strictly via environment variable placeholders (e.g., `${DATAFORSEO_LOGIN}`, `${GSC_REFRESH_TOKEN}`).
3. **Safe OAuth Callback Listeners:**
   - Local OAuth flows (e.g., `vivaak_oauth_flow.py`) bind strictly to `localhost:38888`.
   - The listener immediately terminates after exchanging the authorization code for tokens, preventing persistent open ports.
4. **Git Safety Filters:**
   - The project `.gitignore` explicitly excludes:
     ```gitignore
     .env*
     *.pem
     *credentials*.json
     *service-account*.json
     client_secret*.json
     token*.json
     ```

---

## 4. Client Isolation & Multi-Tenant Boundaries

When the framework is operated across multiple client engagements (e.g., Client A in Industrial Manufacturing, Client B in Luxury Hospitality):

1. **Independent Knowledge Stores:**
   - Each client repository maintains an isolated `knowledge-bank/` and database backend.
   - Prompts for Client B never import facts or entities from Client A.
2. **Distinct Credential Sets:**
   - GSC, GA4, Bing, and Search Engine API credentials are bound strictly per project configuration.
   - Project configuration files define explicit property IDs (e.g., Suntec D1 DB vs Vivaak GA4 Property `475689339`).
3. **Separate Strategic Memories:**
   - Strategic rules learned for industrial B2B manufacturing (e.g., "procurement managers require AMS spec tables") are never blindly transferred to hospitality projects (where emotional sensory descriptions and high-res imagery drive bookings).
4. **Isolated Git Workspaces:**
   - Codebase edits performed by Mechanic operate exclusively in the target client's Git repository and branch.

# Agent Specification: Mechanic (#16)
## Production Code & Infrastructure Engineer

```
========================================================================================
AGENT SPECIFICATION — MECHANIC
========================================================================================
```

### A. Identity
- **Agent Name:** Mechanic
- **Agent ID:** `agent_mechanic`
- **Functional Category:** Layer 5: Infrastructure & Operations (Pool C)
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - Target client codebase (`src/app/`, `components/`)
  - `deploy-cloudflare.sh`
  - `wrangler.json`

---

### B. Purpose
Mechanic is the **sole codebase modification and deployment engineer**. It implements approved content updates, metadata patches, schema blocks, and responsiveness fixes directly into the Next.js production codebase. To guarantee safety, Mechanic operates exclusively in isolated Git branches (`Workspace: branch`) and mandates static build testing before proposing merges.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Modifying Next.js pages, components, CSS styles, and metadata files.
  - Updating CMS database records (Cloudflare D1 SQL or Firebase RTDB).
  - Executing local build verification tests (`npm run build`).
  - Creating isolated Git pull requests and branches.
  - Triggering edge deployments upon explicit human authorization.
- **Out of Scope (Does Not Own):**
  - Deciding content strategy or topics (owned by Editor).
  - Drafting copy or claims (owned by Scribe).
  - Approving production merges autonomously (strict Level C human gate).

---

### D. Capabilities
- **Verified Capabilities:**
  - **Crawl Budget Efficiency Auditing (`CrawlBudgetAuditor`):** Evaluates architectural crawl efficiency, verifying click depth from root ($\le 3$), crawl trap absence (infinite facets, query strings), robots.txt disallow rules against critical assets, and crawler resource consumption (`scripts/search_intelligence_engine.py`).
  - **Index Bloat Detection (`IndexBloatDetector`):** Scans dynamic sitemap and site routes for thin content risks ($< 300$ words), duplicate/boilerplate metadata, parameter variants, and calculates the Index Efficiency Ratio (`scripts/search_intelligence_engine.py`).
  - Isolated Git branch creation (`seo/feature-update-20261013`).
  - Next.js App Router metadata configuration (`generateMetadata` and JSON-LD script tags).
  - SSG build verification testing.
  - Cloudflare Pages / Workers deployment script invocation (`deploy-cloudflare.sh`).
- **Partially Implemented:**
  - Automated visual regression screenshot diffing.
- **Planned Capabilities:**
  - Autonomous edge rollback on HTTP 500 error spikes.

---

### E. Inputs
- **Required Context:** Approved `CONTENT_CHANGE` or `CONTENT_VERSION` from `APPROVAL_QUEUE.md` with human approval timestamp; target Git repository path.
- **Trigger Conditions:** Human approval of a Level B or Level C action.
- **Upstream Dependencies:** Human Growth Director, Sentinel (#3).

---

### F. Tools and Integrations
- `run_command`: Terminal command runner (Git, npm, Wrangler).
- Next.js Build Tools: `npm run build`, `open-next`.
- Cloudflare Wrangler CLI: `wrangler pages deploy`.

---

### G. Processing Logic
1. Verify that action in `APPROVAL_QUEUE.md` is explicitly marked `APPROVED`.
2. Check out a clean, isolated Git branch from `main`:
   ```bash
   git checkout -b seo/patch-act-012
   ```
3. Apply code or database changes:
   - Update metadata export, H1/H2 tags, body copy, and JSON-LD schema block.
4. Execute build verification test:
   ```bash
   npm run build
   ```
5. If build fails:
   - Analyze error stack trace.
   - Fix lint/syntax errors and re-test.
   - Do NOT commit or push broken code.
6. If build passes:
   - Commit changes with descriptive commit message referencing Action ID.
   - Create pull request or notify Human Growth Director for final merge authorization.
7. Upon merge to `main`, invoke deployment script and trigger Courier (#+) for broadcasting.

---

### H. Outputs
- **Format:** Committed Git branch, build test verification logs, deployment status.
- **Downstream Consumer:** Courier ([+]) for fast indexing pings.

---

### I. Inter-Agent Communication
- **Triggered By:** Human Director (via `APPROVAL_QUEUE.md`).
- **Calls:** Courier ([+]) upon deployment completion.

---

### J. Memory and Persistence
- **Reads:** Approved change manifests from `data/approvals/`.
- **Writes:** Git commit history and build log records.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level C (Strict Mutex Concurrency, Pool C).
- **Hard Gate:** Never commits directly to `main` without human confirmation. Never deploys unverified code.

---

### L. Error Handling
- **Build Failure:** Reverts working tree, captures error log, and flags task as `BUILD_ERROR` for developer inspection.

---

### M. Evaluation
- Evaluated on achieving 100% clean builds on production edge without breaking existing layouts or routes.

---

### N. Limitations
- Limited by build environment memory and Node.js package configurations.

---

### O. Extension Guide
To support a new frontend framework (e.g. Astro, Remix, Hugo), configure the build and deployment commands in `config/project-configuration.json`.

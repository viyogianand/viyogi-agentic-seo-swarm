# Security Policy
## Reporting Vulnerabilities, Client Data Isolation & Secret Safety

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — SECURITY POLICY
========================================================================================
```

## 1. Supported Versions

| Version | Supported | Security Maintenance Status |
| :---: | :---: | :--- |
| **3.1.x** | **Yes** | Active development; all security patches applied. |
| **3.0.x** | **Yes** | Active security support. |
| **2.0.x** | Limited | Critical vulnerability patches only. |
| **1.0.x** | No | Legacy prototype; upgrade to V3.1 recommended. |

---

## 2. Core Security & Privacy Commitments

1. **Zero Secret Leaks in Public Repositories:**
   - Real API keys, tokens, client secrets, and database connection strings must **never** be committed to Git.
   - All code repositories must enforce `.gitignore` rules covering `.env*`, `*credentials*.json`, and `*service-account*.json`.
2. **Strict Multi-Tenant Client Isolation:**
   - The framework maintains complete separation between clients. Prompts, memory vectors, and Knowledge Bank stores are strictly sandboxed per workspace directory.
   - No customer or proprietary business data is shared across client environments.
3. **No Autonomous External Actions:**
   - Agents are architecturally barred from sending emails (`Networker` drafts locally only), spending capital, or purchasing backlinks.
   - Production codebase merges and deployments require human authorization in `APPROVAL_QUEUE.md`.
4. **Sandboxed OAuth Listeners:**
   - The local OAuth helper (`scripts/vivaak_oauth_flow.py`) listens exclusively on `localhost:38888` and terminates immediately after token exchange.

---

## 3. Reporting a Security Vulnerability

If you discover a security vulnerability, credential exposure, or client data isolation issue in the Viyogi Agentic SEO Swarm:

1. **Do NOT open a public GitHub issue.**
2. Send a detailed report to the security maintainers:
   - Email: `security@viyogi.com` or contact the system owner directly.
   - Include a description of the issue, affected files, and proof-of-concept steps.
3. We will acknowledge receipt within 48 hours and work with you to release a coordinated patch.

# Troubleshooting & Common Issues
## Diagnosing and Resolving Installation, API, and Execution Errors

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — TROUBLESHOOTING GUIDE
========================================================================================
```

## 1. Common Issues & Solutions

### 1.1 "Address already in use: localhost:38888" during OAuth
- **Cause:** A previous instance of `vivaak_oauth_flow.py` is still listening on port 38888.
- **Solution:**
  Find and terminate the process:
  ```bash
  lsof -ti:38888 | xargs kill -9
  ```
  Then re-run:
  ```bash
  python3 scripts/vivaak_oauth_flow.py
  ```

---

### 1.2 DataForSEO HTTP 401 Unauthorized / Insufficient Balance
- **Cause:** Invalid `DATAFORSEO_LOGIN` or `DATAFORSEO_PASSWORD`, or account balance is \$0.00.
- **Solution:**
  1. Check your credentials in `.env.local`.
  2. Verify your balance in the [DataForSEO Dashboard](https://app.dataforseo.com).
  3. Note: Basic auth requires `login:password` base64-encoded.

---

### 1.3 Google Search Console API Returns 403 Forbidden
- **Cause:** The authorized Google account does not have verified owner/full permissions on the target property.
- **Solution:**
  1. Open [Google Search Console](https://search.google.com/search-console).
  2. Verify that your email has at least "Full" access to the domain property (`sc-domain:example.com`).
  3. Ensure the exact property string matches (e.g. `sc-domain:vivaak.com` vs `https://vivaak.com/`).

---

### 1.4 Next.js SSG Build Failure during Mechanic Check
- **Cause:** `npm run build` fails due to unhandled TypeScript errors or missing static parameters in `generateStaticParams`.
- **Solution:**
  1. Mechanic automatically isolates this in a feature branch.
  2. Run the build locally to inspect the compiler error:
     ```bash
     npm run build
     ```
  3. Ensure all dynamic parameters (e.g. blog slugs) have corresponding entries in `generateStaticParams()`.

---

### 1.5 Sentinel Repeatedly Rejects Content Drafts
- **Cause:** Scribe is using banned marketing buzzwords or making ungrounded claims not listed in Archivist's facts.
- **Solution:**
  1. Inspect Sentinel's audit diff in the rejection log.
  2. If the claim is factually true, add the verified fact to `knowledge-bank/products-and-services.json`.
  3. If Scribe used banned words (e.g. *"nestled in nature"*), review `knowledge-bank/human-writing-guide.md` and prompt Scribe with the explicit banned list.

---

### 1.6 IndexNow Returns HTTP 422 Unprocessable Entity
- **Cause:** The verification key text file hosted on your public site does not match the key specified in the API request.
- **Solution:**
  1. Verify the public URL:
     ```bash
     curl -i https://example.com/8a4b0421cd964dfcabd3a7b2ef122ce0.txt
     ```
  2. Ensure the response body contains only the exact key string with no extra HTML or whitespace.

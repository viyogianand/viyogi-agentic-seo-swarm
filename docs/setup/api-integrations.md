# API Integrations & Tool Setup
## Configuring DataForSEO, Google OAuth 2.0, Bing Webmaster & IndexNow

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — API INTEGRATIONS GUIDE
========================================================================================
```

## 1. Setting Up the Google Cloud OAuth 2.0 Listener

The swarm accesses Google Search Console, Google Analytics 4, Google Tag Manager, Google Indexing API, and Google Business Profile through a unified OAuth 2.0 flow.

### Step-by-Step Google OAuth Configuration:
1. Open the [Google Cloud Console](https://console.cloud.google.com).
2. Create or select your project (e.g. `seo-growth-system`).
3. Enable the following APIs under **APIs & Services ➔ Library**:
   - Google Search Console API (Webmasters API)
   - Google Analytics Data API
   - Google Tag Manager API
   - Web Search Indexing API
   - Google Business Profile Management API (`business.manage`)
4. Go to **Credentials ➔ Create Credentials ➔ OAuth client ID**:
   - Application type: **Web application**
   - Name: `antigravity-seo-swarm`
   - Authorized redirect URIs: Add `http://localhost:38888`
5. Note your **Client ID** and **Client Secret**.
6. Launch the local OAuth listener:
   ```bash
   python3 scripts/vivaak_oauth_flow.py
   ```
7. Visit `http://localhost:38888` in your browser, select your Google account, and grant permissions.
8. The listener automatically saves tokens to `~/.gemini/config/google-credentials.json` and updates `~/.gemini/config/mcp_config.json`.

---

## 2. Configuring DataForSEO

DataForSEO powers live SERP tracking, keyword volumes, and backlink analysis.
1. Sign up at [dataforseo.com](https://dataforseo.com).
2. Fund your account with pay-per-call balance.
3. Add your login and API password to `.env.local`:
   ```bash
   DATAFORSEO_LOGIN="your-email@example.com"
   DATAFORSEO_PASSWORD="your-api-password"
   ```
4. Verify connectivity:
   ```bash
   python3 scripts/keyword_planner.py --test-connection
   ```

---

## 3. Configuring Bing Webmaster Tools & IndexNow

1. Log into [Bing Webmaster Tools](https://www.bing.com/webmasters).
2. Verify domain ownership (fast 1-click import from Google Search Console).
3. Obtain API Key from **Settings ➔ API Access ➔ API Key**.
4. Generate an IndexNow Key (or use an existing 32-character hex string).
5. Host the key text file at the root of your public website (e.g. `https://example.com/8a4b0421cd964dfcabd3a7b2ef122ce0.txt`).
6. Test broadcast:
   ```bash
   python3 scripts/submit_indexnow.py https://example.com/test-page
   ```

---

## 4. Behavior When an Integration is Missing

The framework is resilient to missing API credentials:
- If `DATAFORSEO_LOGIN` is absent, Scout and Prospector fall back to first-party GSC telemetry.
- If `FIRECRAWL_API_KEY` is absent, Shadow falls back to standard HTTP requests with the local `RobustHTMLParser`.
- If `BING_INDEXNOW_KEY` is absent, Courier skips IndexNow broadcasting and logs a skip notice.
- Missing data is always marked with `Evidence State: UNKNOWN` rather than halting the swarm.

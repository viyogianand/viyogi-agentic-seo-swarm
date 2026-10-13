# Environment Variables Reference
## Secure Configuration of API Keys, Tokens & Database Credentials

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — ENVIRONMENT VARIABLES REFERENCE
========================================================================================
```

> [!CAUTION]
> **Security Protocol:** Never commit real API keys, tokens, or passwords to Git. Store local credentials strictly in `.env.local` or user-level config files (`~/.gemini/config/`).

---

## 1. Master Environment Variable Inventory

| Variable Name | Required? | Category | Description | Where to Obtain |
| :--- | :---: | :--- | :--- | :--- |
| `DATAFORSEO_LOGIN` | **Yes** | DataForSEO | Email or account login for DataForSEO. | [DataForSEO Dashboard](https://dataforseo.com) |
| `DATAFORSEO_PASSWORD` | **Yes** | DataForSEO | API password / secret for DataForSEO. | [DataForSEO API Access](https://app.dataforseo.com/api-dashboard) |
| `GSC_CLIENT_ID` | **Yes** | Google OAuth | OAuth 2.0 Web Client ID for Google APIs. | Google Cloud Console ➔ APIs & Services ➔ Credentials |
| `GSC_CLIENT_SECRET` | **Yes** | Google OAuth | OAuth 2.0 Client Secret. | Google Cloud Console |
| `GSC_REFRESH_TOKEN` | **Yes** | Google OAuth | Persistent refresh token generated via OAuth flow. | Emitted by `vivaak_oauth_flow.py` |
| `GA4_PROPERTY_ID` | **Yes** | Analytics | Numeric Property ID of the connected GA4 container. | Google Analytics ➔ Admin ➔ Property Settings |
| `BING_WEBMASTER_API_KEY`| No | Bing | API key for Bing Webmaster Tools rank/crawl data. | [Bing Webmaster Tools](https://www.bing.com/webmasters) ➔ Settings ➔ API Access |
| `BING_INDEXNOW_KEY` | No | IndexNow | 32-character hex key hosted at website root. | Generated in Bing Webmaster Tools / IndexNow |
| `FIRECRAWL_API_KEY` | No | Scraper | API key for Firecrawl Markdown extraction. | [Firecrawl.dev](https://firecrawl.dev) |
| `CLOUDFLARE_API_TOKEN` | No | Edge Deploy | Token with Pages and Workers deployment permissions. | Cloudflare Dashboard ➔ My Profile ➔ API Tokens |
| `CLOUDFLARE_ACCOUNT_ID`| No | Edge Deploy | Cloudflare account identifier. | Cloudflare Dashboard Overview sidebar |

---

## 2. Sanitized Example `.env.example`

```bash
# ==============================================================================
# VIYOGI AGENTIC SEO SWARM — ENVIRONMENT CONFIGURATION TEMPLATE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DATAFORSEO API CREDENTIALS
# ------------------------------------------------------------------------------
DATAFORSEO_LOGIN="your-email@example.com"
DATAFORSEO_PASSWORD="your-dataforseo-api-password"

# ------------------------------------------------------------------------------
# 2. GOOGLE CLOUD OAUTH 2.0 CREDENTIALS (GSC, GA4, GBP, INDEXING)
# ------------------------------------------------------------------------------
GSC_CLIENT_ID="851121485187-xxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com"
GSC_CLIENT_SECRET="GOCSPX-xxxxxxxxxxxxxxxxxxxxxxxx"
GSC_REFRESH_TOKEN="1//0gtxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GA4_PROPERTY_ID="475689339"

# ------------------------------------------------------------------------------
# 3. BING WEBMASTER TOOLS & INDEXNOW
# ------------------------------------------------------------------------------
BING_WEBMASTER_API_KEY="84fbcc2777f642a9be3faef0a4a45ae1"
BING_INDEXNOW_KEY="8a4b0421cd964dfcabd3a7b2ef122ce0"

# ------------------------------------------------------------------------------
# 4. SCRAPING & CRAWLING
# ------------------------------------------------------------------------------
FIRECRAWL_API_KEY="fc-xxxxxxxxxxxxxxxxxxxxxxxx"

# ------------------------------------------------------------------------------
# 5. CLOUDFLARE EDGE DEPLOYMENT (OPTIONAL)
# ------------------------------------------------------------------------------
CLOUDFLARE_API_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
CLOUDFLARE_ACCOUNT_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

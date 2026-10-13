# Cost & Token Management
## Budget Allocation, API Costs & Operational Optimization

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — COST MANAGEMENT SPECIFICATION
========================================================================================
```

## 1. Cost Drivers & Financial Model

Running an autonomous 22-agent SEO department incurs two categories of ongoing operational expense:
1. **LLM Reasoning Tokens:** API costs from Google Gemini, Anthropic Claude, or OpenAI models.
2. **Third-Party SEO API Calls:** Pay-per-call charges from DataForSEO, Firecrawl, and proxy networks.

```
┌────────────────────────────────────────────────────────────────────────┐
│ MONTHLY ESTIMATED COST BREAKDOWN (Active Production Project)           │
│ • LLM Reasoning Tokens (Tiered Flash + Pro): ~\$8.00 - \$22.00 / mo    │
│ • DataForSEO SERP & Volume APIs (Batched): ~\$12.00 - \$28.00 / mo     │
│ • Firecrawl Scrapes (Targeted Competitors): ~\$4.00 - \$10.00 / mo     │
│ • Google Search Console, GA4 & Bing APIs: \$0.00 (Free / Official)     │
│ • IndexNow Protocol & Google Indexing: \$0.00 (Free)                   │
│ ➔ TOTAL MONTHLY OPERATIONAL RUN RATE: ~\$24.00 - \$60.00 / month       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Token Allocation Rules

To prevent unexpected API billing spikes:
1. **Token Budgets per Turn:**
   - Flash workers (Pool A): Maximum 2,000 output tokens.
   - Scribe (Long-form drafting): Maximum 4,000 output tokens.
   - Conductor (Strategic planning): Maximum 3,000 output tokens.
2. **Context Window Hygiene:**
   - Raw HTML is stripped before ingestion (saves 85% of input tokens).
   - Knowledge Bank facts are cached rather than re-summarized each cycle.
   - Intermediate agent communication uses compact JSON instead of verbose conversational markdown.

---

## 3. API Call Batching

DataForSEO charges per request. The framework enforces strict batching:
- **Never:** Single-keyword SERP calls (50 keywords = 50 API calls = \$0.30).
- **Enforced:** Multi-item batched requests (50 keywords in 1 batched call = \$0.06).
- **Result:** Reduces third-party API costs by 75–80%.

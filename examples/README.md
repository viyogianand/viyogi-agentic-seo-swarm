# Example Implementations & Reference Profiles
## Sanitized Production Blueprints from Real-World Swarm Deployments

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — EXAMPLE IMPLEMENTATIONS
========================================================================================
```

This directory provides two sanitized, reference configurations based directly on the empirical deployments audited during the framework's development:

| Example Profile | Target Vertical | Key Architectural Focus |
| :--- | :--- | :--- |
| **[`b2b-industrial-suntec/`](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/examples/b2b-industrial-suntec/README.md)** | B2B Industrial Manufacturing (Cut Wire Shot) | Heavy metallurgical specifications, AMS/DIN/ISO standards, Cloudflare D1 SQL integration, global export demand capture (India, Germany, US). |
| **[`hospitality-vivaak/`](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/examples/hospitality-vivaak/README.md)** | Luxury Boutique Hospitality & Villas | Sensory experiential drafting, heated pool/jacuzzi proof points, Google Maps Local 3-Pack, Localist agent, Firebase RTDB + Next.js SSG. |

---

## How to Use These Examples

To use either profile as a template for your business:
1. Copy the relevant directory contents into your project's `config/` and `knowledge-bank/` directories:
   ```bash
   cp -r examples/b2b-industrial-suntec/knowledge-bank/* knowledge-bank/
   cp examples/b2b-industrial-suntec/project-configuration.json config/
   ```
2. Replace entity names, physical addresses, phone numbers, and product specifications with your verified corporate data.
3. Validate completeness via `python3 schemas/v3_1/validator.py`.

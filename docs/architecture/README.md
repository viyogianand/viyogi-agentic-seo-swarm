# System Architecture Documentation

Welcome to the architectural specifications for **Viyogi Agentic SEO Swarm**, a multi-agent framework designed for evidence-based search, answer engine (AEO), generative engine (GEO), and local search optimization.

## Document Directory

| Document | Purpose |
| :--- | :--- |
| **[Architecture Overview](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/architecture-overview.md)** | Core design philosophy, 3-layer separation, 18-step decision loop, and North Star metrics. |
| **[Agent Topology](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/agent-topology.md)** | 5-layer organization of the 22 canonical agents and Pool A/B/C execution model. |
| **[Data Flow](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/data-flow.md)** | End-to-end data lifecycle from telemetry/crawl/SERP to drafting, verification, and deployment. |
| **[Memory & Knowledge](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/memory-and-knowledge.md)** | 4-level Strategic Memory model, knowledge bank interface, and fact verification caching. |
| **[Model Routing](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/model-routing.md)** | Tiered LLM routing protocol, token-optimization practices, and runtime cost controls. |
| **[Security & Permissions](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/security-and-permissions.md)** | 3-tier governance protocol (Level A/B/C), client data isolation, and credential security. |
| **[Technology Stack](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/tech-stack.md)** | Runtime environment, languages, APIs, MCP servers, storage adapters, and deployment edge. |
| **[Architecture Reconciliation](file:///Users/viyogianand/Desktop/Presonal%20Pratyush/viyogi-agentic-seo-swarm/docs/architecture/architecture-reconciliation.md)** | Comparative audit cross-referencing Suntec Enterprises and VivaakVaza source projects. |

---

## Architectural Principles at a Glance

1. **Commercial Intent Over Raw Volume:** The swarm optimizes for high-intent inquiries, RFQs, bookings, and verified commercial engagement rather than vanity pageviews.
2. **Anti-Hallucination Guardrails:** Sentinel exercises strict veto authority over unverified specifications, false claims, and schema defects.
3. **Decoupled Business Knowledge:** Agent reasoning logic is completely separated from business-specific domain facts and constraints.
4. **Token-Efficiency First:** Stateless Intelligence Engines execute mechanical calculations; high-cost reasoning models are reserved strictly for strategic decisions and drafting.
5. **No Blind Automation:** Strict human-in-the-loop approvals (`APPROVAL_QUEUE.md`) are enforced for code merges, production releases, external outreach, and capital allocations.

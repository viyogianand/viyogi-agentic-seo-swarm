# Agent Specification: Herald (#19)
## Industry News & Event Intelligence Specialist

```
========================================================================================
AGENT SPECIFICATION — HERALD
========================================================================================
```

### A. Identity
- **Agent Name:** Herald
- **Agent ID:** `agent_herald`
- **Functional Category:** Layer 5: Infrastructure & Operations
- **Implementation Status:** Verified & Operational
- **Source Project:** Suntec Enterprises & VivaakVaza
- **Relevant Implementation Files:**
  - `Suntec_Global_Industrial_Events_Report.md`
  - `Suntec_Global_Industrial_Events_Calendar.xlsx`
  - `data/events/`

---

### B. Purpose
Herald aligns the swarm's content velocity with real-world industry events, seasonal buyer demand rhythms, and company milestones. Whether covering premier international industrial trade fairs (e.g. ANKIROS 2026, GIFA) or seasonal travel rhythms (winter snowfall getaways, monsoon retreats), Herald turns real-world events into high-authority topical search assets.

---

### C. Responsibilities
- **In Scope (Owns):**
  - Tracking international and domestic trade exhibitions, conferences, and festivals.
  - Analyzing exhibitor intelligence, hall directories, and attendee buyer profiles.
  - Aligning editorial publishing schedules with peak seasonal search demand.
  - Drafting event previews, buyer guides, and post-event intelligence summaries.
- **Out of Scope (Does Not Own):**
  - Drafting technical specification sheets (owned by Scribe).
  - Registering booths or spending sponsorship capital (strict Level C action).

---

### D. Capabilities
- **Verified Capabilities:**
  - Processing exhibitor directories (e.g. 1,000+ exhibitors from ANKIROS 2026 Istanbul) and filtering by buyer relevance.
  - Generating seasonal editorial content calendars.
  - Transforming exhibition attendance into authoritative industry buyer guide articles.
- **Partially Implemented:**
  - Automated tracking of trade show website exhibitor list updates.
- **Planned Capabilities:**
  - Automated integration with event ticketing and calendar APIs.

---

### E. Inputs
- **Required Context:** Annual event dates; seasonal demand curves; target product lines or property locations.
- **Trigger Conditions:** 60 days prior to major industry event or seasonal demand surge.
- **Upstream Dependencies:** Conductor, Knowledge Bank.

---

### F. Tools and Integrations
- `EventIntelligenceEngine`: Parses exhibitor directories and schedules.
- Seasonal Demand Calendar (`data/events/calendar.json`).

---

### G. Processing Logic
1. Monitor upcoming events in the calendar (e.g., ANKIROS trade fair 60 days out).
2. Filter event attendee profiles for target buyers (plant managers, foundry heads, procurement leads).
3. Identify relevant search queries trending around the event:
   - "cut wire shot suppliers at ANKIROS 2026", "foundry trade shows europe 2026".
4. Brief Editor (#20) to commission targeted preview articles and buyer guides.
5. Post-event: Synthesize key industry trends observed on the ground into a permanent authoritative market report.

---

### H. Outputs
- **Format:** Event Intelligence Reports and Seasonal Content Schedules.
- **Example Artifact:**
  - `docs/reports/Global_Industrial_Events_Report.md`
  - `data/events/event_brief_ankiros2026.json`

---

### I. Inter-Agent Communication
- **Collaborates With:** Editor (#20) (content scheduling), Scribe (#12) (event guide drafting).
- **Reports To:** Conductor (#1).

---

### J. Memory and Persistence
- **Reads:** Event calendar from `knowledge-bank/`.
- **Writes:** Stores historical event intelligence records in Strategic Memory.

---

### K. Autonomy and Permissions
- **Autonomy Tier:** Level A (Event monitoring, directory filtering, and editorial scheduling).

---

### L. Error Handling
- **Event Cancellation / Date Shift:** Updates internal calendar, notifies Conductor, and adjusts downstream editorial deadlines.

---

### M. Evaluation
- Evaluated on whether event-aligned content ranks for event-specific buyer queries ahead of opening day.

---

### N. Limitations
- Relies on published event organizer directories; cannot predict unannounced conference schedules.

---

### O. Extension Guide
To configure for a new business, add industry events or seasonal customer rhythms to `knowledge-bank/events-and-seasons.json`.

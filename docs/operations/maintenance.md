# Ongoing Maintenance & System Upkeep
## Routine Procedures, Database Backups & Model Deprecation Handling

```
========================================================================================
VIYOGI AGENTIC SEO SWARM — MAINTENANCE SPECIFICATION
========================================================================================
```

## 1. Routine Maintenance Schedule

| Maintenance Task | Frequency | Automated vs Manual | Procedure |
| :--- | :---: | :---: | :--- |
| **Database & Knowledge Bank Backup** | Weekly | Automated Script | `python3 scripts/backup_d1_database.py` exports SQL/JSON snapshot to `backup/`. |
| **Google OAuth Token Refresh Check** | Bi-weekly | Automated / Alert | Validates refresh token validity against Google OAuth token endpoint. |
| **Competitor Domain Review** | Monthly | Manual Review | Review tracked competitor URLs; add newly emerging competitors to `competitors.json`. |
| **Strategic Memory Pruning** | Quarterly | Automated / Conductor | Consolidates redundant Level 2 observations into permanent Level 3 learnings. |
| **LLM Model Deprecation Audit** | Quarterly | Developer Review | Verifies active model IDs against Google / Anthropic deprecation schedules. |

---

## 2. Database Backup & Restore Protocols

### Cloudflare D1 Relational Backup
```bash
# Automated via scripts/backup-schema.sh
npx wrangler d1 export suntech_cms --output backup/backup_$(date +%Y%m%d).sql
```

### Firebase RTDB Snapshot
```bash
python3 -c "
import urllib.request, json
# Pulls snapshot via admin secret or export script
"
```

---

## 3. Handling Search Engine Core Updates

When Google or Bing announces a major core algorithm update:
1. Conductor enters **Observation Hold** mode for 14 days.
2. In-flight 28-day experiments are marked `CORE_UPDATE_SUSPENDED` to prevent false causal attribution.
3. Scout increases rank tracking frequency to daily to map keyword volatility bands.
4. After SERP stabilization, Forecaster re-baselines targets and resumes experimental cycles.

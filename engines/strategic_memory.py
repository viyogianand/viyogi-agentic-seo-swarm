#!/usr/bin/env python3
"""
Strategic Memory Engine (V2.0)
Manages the 4-Level Bayesian Strategic Memory:
Level 1: Ground-Truth Facts
Level 2: Empirical Observations
Level 3: Causal Learnings
Level 4: Strategic Rules
Also manages Opportunity Cards, Experiment Cards, and Rejections Registry.
"""

import os
import json
import sqlite3
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, "strategic_memory.db")
JSON_PATH = os.path.join(DATA_DIR, "strategic_memory.json")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_schema():
    conn = get_db()
    cur = conn.cursor()
    
    # Level 1: Ground-Truth Facts
    cur.execute("""
    CREATE TABLE IF NOT EXISTS strategic_facts (
        fact_id TEXT PRIMARY KEY,
        category TEXT NOT NULL, -- ENTITY, METALLURGY, STANDARD, FACILITY, POLICY
        subject TEXT NOT NULL,
        fact_value TEXT NOT NULL,
        verification_source TEXT NOT NULL,
        immutable INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Level 2: Empirical Observations
    cur.execute("""
    CREATE TABLE IF NOT EXISTS strategic_observations (
        obs_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        source TEXT NOT NULL, -- GSC, GA4, DATAFORSEO, FIRECRAWL
        metric_name TEXT NOT NULL,
        metric_value REAL,
        query TEXT,
        url TEXT,
        evidence_level TEXT NOT NULL, -- OBSERVED, MEASURED
        confidence TEXT NOT NULL,
        observed_at TIMESTAMP NOT NULL,
        metadata_json TEXT
    );
    """)

    # Level 3: Causal Learnings
    cur.execute("""
    CREATE TABLE IF NOT EXISTS strategic_learnings (
        learning_id TEXT PRIMARY KEY,
        experiment_id TEXT,
        topic_cluster TEXT NOT NULL,
        learning_statement TEXT NOT NULL,
        supporting_evidence TEXT NOT NULL,
        confidence TEXT NOT NULL, -- HIGH, MEDIUM, LOW
        promoted_from_obs_count INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Level 4: Strategic Rules
    cur.execute("""
    CREATE TABLE IF NOT EXISTS strategic_rules (
        rule_id TEXT PRIMARY KEY,
        rule_name TEXT NOT NULL,
        condition_scope TEXT NOT NULL,
        directive TEXT NOT NULL,
        validation_clusters TEXT NOT NULL, -- e.g. "foundational, comparisons"
        status TEXT DEFAULT 'ACTIVE', -- ACTIVE, UNDER_INVESTIGATION, DEPRECATED
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Rejection Memory
    cur.execute("""
    CREATE TABLE IF NOT EXISTS strategic_rejections (
        rejection_id TEXT PRIMARY KEY,
        topic TEXT NOT NULL,
        proposed_query TEXT NOT NULL,
        rejected_by TEXT NOT NULL,
        rejection_category TEXT NOT NULL,
        rationale TEXT NOT NULL,
        review_after_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Content Opportunity Cards
    cur.execute("""
    CREATE TABLE IF NOT EXISTS content_opportunity_cards (
        opportunity_id TEXT PRIMARY KEY,
        topic TEXT NOT NULL,
        primary_query TEXT NOT NULL,
        search_intent TEXT NOT NULL,
        buyer_intent TEXT NOT NULL,
        commercial_value REAL NOT NULL,
        current_suntec_page TEXT,
        current_ranking REAL,
        current_impressions_28d INTEGER,
        current_ctr REAL,
        recommended_action TEXT NOT NULL,
        card_json TEXT NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Experiments Registry
    cur.execute("""
    CREATE TABLE IF NOT EXISTS experiments_registry (
        experiment_id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        target_url TEXT NOT NULL,
        test_type TEXT NOT NULL,
        hypothesis TEXT NOT NULL,
        status TEXT NOT NULL, -- PROPOSED, APPROVED, ACTIVE_MEASURING, COMPLETED, REVERTED
        baseline_json TEXT NOT NULL,
        intervention_json TEXT NOT NULL,
        results_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Forecasts Registry
    cur.execute("""
    CREATE TABLE IF NOT EXISTS forecasts_registry (
        forecast_id TEXT PRIMARY KEY,
        target_query TEXT NOT NULL,
        target_url TEXT NOT NULL,
        target_market TEXT NOT NULL,
        baseline_position REAL,
        p10_weeks INTEGER,
        p50_weeks INTEGER,
        p90_weeks INTEGER,
        confidence TEXT NOT NULL,
        prerequisites_json TEXT NOT NULL,
        forecast_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # --- BACKLINK & DIGITAL AUTHORITY SUBSYSTEM TABLES ---
    
    # 1. Backlink Prospects
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_prospects (
        prospect_id TEXT PRIMARY KEY,
        organization TEXT NOT NULL,
        domain TEXT NOT NULL UNIQUE,
        url TEXT NOT NULL,
        country TEXT NOT NULL,
        language TEXT DEFAULT 'en',
        industry TEXT NOT NULL,
        website_type TEXT NOT NULL, -- TRADE_PUBLICATION, ASSOCIATION, DIRECTORY, OEM_PARTNER, UNIVERSITY, MEDIA
        audience TEXT,
        relevance_score REAL NOT NULL,
        authority_score REAL NOT NULL,
        dataforseo_rank INTEGER,
        organic_visibility REAL,
        estimated_traffic REAL,
        spam_risk REAL NOT NULL,
        editorial_fit REAL NOT NULL,
        commercial_relevance REAL NOT NULL,
        geographic_relevance REAL NOT NULL,
        relationship_potential REAL NOT NULL,
        overall_score REAL NOT NULL,
        priority TEXT NOT NULL, -- P0_STRATEGIC, P1_HIGH, P2_GOOD, P3_INVESTIGATE, P4_REJECT
        status TEXT NOT NULL, -- DISCOVERED, QUALIFIED, CONTACT_IDENTIFIED, OUTREACH_READY, OUTREACH_SENT, ACCEPTED, ACQUIRED, REJECTED
        discovery_source TEXT NOT NULL,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Backlink Contacts
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_contacts (
        contact_id TEXT PRIMARY KEY,
        prospect_id TEXT NOT NULL,
        name TEXT NOT NULL,
        job_title TEXT NOT NULL,
        organization TEXT NOT NULL,
        email TEXT,
        email_status TEXT NOT NULL, -- VERIFIED, PROBABLE, UNVERIFIED, NOT_FOUND
        linkedin_url TEXT,
        contact_page TEXT,
        source_url TEXT NOT NULL,
        contact_evidence TEXT,
        outreach_status TEXT DEFAULT 'PENDING',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (prospect_id) REFERENCES backlink_prospects (prospect_id)
    );
    """)

    # 3. Backlink Opportunities
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_opportunities (
        opportunity_id TEXT PRIMARY KEY,
        prospect_id TEXT NOT NULL,
        opportunity_type TEXT NOT NULL, -- COMPETITOR_LINK_GAP, RESOURCE_PAGE, EDITORIAL_MENTION, EXPERT_COMMENTARY, BROKEN_LINK, PARTNERSHIP
        target_url TEXT NOT NULL,
        target_keyword_cluster TEXT NOT NULL,
        why_it_matters TEXT NOT NULL,
        proposed_value TEXT NOT NULL,
        suggested_pitch TEXT NOT NULL,
        suggested_anchor TEXT NOT NULL,
        acquisition_difficulty REAL NOT NULL,
        expected_value REAL NOT NULL,
        confidence REAL NOT NULL,
        priority TEXT NOT NULL,
        status TEXT DEFAULT 'IDENTIFIED',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (prospect_id) REFERENCES backlink_prospects (prospect_id)
    );
    """)

    # 4. Backlink Outreach
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_outreach (
        outreach_id TEXT PRIMARY KEY,
        prospect_id TEXT NOT NULL,
        contact_id TEXT,
        opportunity_id TEXT NOT NULL,
        subject TEXT NOT NULL,
        message TEXT NOT NULL,
        value_proposition TEXT NOT NULL,
        channel TEXT DEFAULT 'EMAIL',
        status TEXT DEFAULT 'DRAFTED', -- DRAFTED, APPROVED, SENT, REPLIED, NEGOTIATING, ACCEPTED, DECLINED, NO_RESPONSE
        approval_status TEXT DEFAULT 'PENDING_HUMAN_APPROVAL',
        date_sent TEXT,
        follow_up_date TEXT,
        follow_up_count INTEGER DEFAULT 0,
        response TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (prospect_id) REFERENCES backlink_prospects (prospect_id)
    );
    """)

    # 5. Acquired Backlinks
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_acquired (
        link_id TEXT PRIMARY KEY,
        prospect_id TEXT NOT NULL,
        opportunity_id TEXT,
        source_url TEXT NOT NULL,
        target_url TEXT NOT NULL,
        anchor TEXT NOT NULL,
        link_attribute TEXT DEFAULT 'dofollow', -- dofollow, nofollow, sponsored, ugc
        http_status INTEGER DEFAULT 200,
        is_live INTEGER DEFAULT 1,
        referral_sessions INTEGER DEFAULT 0,
        first_verified_at TEXT NOT NULL,
        last_verified_at TEXT NOT NULL,
        FOREIGN KEY (prospect_id) REFERENCES backlink_prospects (prospect_id)
    );
    """)

    # 6. Lost Backlinks
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_lost (
        loss_id TEXT PRIMARY KEY,
        source_url TEXT NOT NULL,
        target_url TEXT NOT NULL,
        referring_domain TEXT NOT NULL,
        reason TEXT NOT NULL, -- 404_PAGE, LINK_REMOVED, REDIRECTED, DOMAIN_EXPIRED
        recovery_priority TEXT NOT NULL, -- HIGH, MEDIUM, LOW
        recovery_status TEXT DEFAULT 'IDENTIFIED',
        lost_detected_at TEXT NOT NULL
    );
    """)

    # 7. Competitor Link Gaps
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_competitor_gaps (
        gap_id TEXT PRIMARY KEY,
        referring_domain TEXT NOT NULL UNIQUE,
        competitors_linked_json TEXT NOT NULL, -- ["winoa.com", "pelletsllc.com"]
        intersection_count INTEGER NOT NULL,
        domain_rank INTEGER,
        estimated_authority REAL,
        opportunity_type TEXT NOT NULL,
        status TEXT DEFAULT 'UNRESOLVED',
        discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 8. Linkable Assets Registry
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_linkable_assets (
        asset_id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        asset_type TEXT NOT NULL, -- GUIDE, CALCULATOR, STANDARDS_DB, COMPARISON_CHART, ORIGINAL_DATA
        seo_value REAL NOT NULL,
        commercial_value REAL NOT NULL,
        linkability_score REAL NOT NULL,
        pr_potential REAL NOT NULL,
        resource_potential REAL NOT NULL,
        overall_asset_score REAL NOT NULL,
        status TEXT DEFAULT 'ACTIVE',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 9. Backlink Learnings Registry
    cur.execute("""
    CREATE TABLE IF NOT EXISTS backlink_learnings (
        learning_id TEXT PRIMARY KEY,
        campaign_name TEXT NOT NULL,
        channel TEXT NOT NULL,
        prospects_count INTEGER NOT NULL,
        response_rate REAL NOT NULL,
        acquisition_rate REAL NOT NULL,
        learning_insight TEXT NOT NULL,
        recommended_adjustment TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # --- SEARCH INTELLIGENCE & TECHNICAL SEO AUTONOMY SUBSYSTEM TABLES ---

    # 1. Query Fan-Out Intelligence
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_query_fanout (
        fanout_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        seed_query TEXT NOT NULL,
        target_market TEXT NOT NULL,
        fanout_tree_json TEXT NOT NULL,
        total_nodes INTEGER NOT NULL,
        observed_nodes_count INTEGER NOT NULL,
        modeled_nodes_count INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Information Gain Analysis
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_information_gain (
        gain_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        target_query TEXT NOT NULL,
        target_url TEXT NOT NULL,
        information_gain_score REAL NOT NULL,
        novel_data_score REAL NOT NULL,
        comparison_utility_score REAL NOT NULL,
        depth_completeness_score REAL NOT NULL,
        answer_directness_score REAL NOT NULL,
        competitor_gaps_json TEXT NOT NULL,
        recommended_interventions_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. Keyword Cannibalization Detection
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_cannibalization_findings (
        finding_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        query TEXT NOT NULL,
        primary_url TEXT NOT NULL,
        conflicting_url TEXT NOT NULL,
        severity TEXT NOT NULL, -- CRITICAL, HIGH, MODERATE, LOW
        similarity_score REAL NOT NULL,
        rank_primary REAL,
        rank_conflicting REAL,
        recommended_action TEXT NOT NULL, -- CANONICAL_CONSOLIDATION, 301_REDIRECT, DE_OPTIMIZE_SECONDARY, CONTENT_MERGE
        approval_status TEXT DEFAULT 'PENDING_HUMAN_APPROVAL',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 4. Crawl Budget & Architecture Analysis
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_crawl_budget_audits (
        audit_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        evidence_level TEXT DEFAULT 'SIMULATED_ARCHITECTURAL',
        data_source TEXT NOT NULL,
        total_urls_audited INTEGER NOT NULL,
        max_click_depth INTEGER NOT NULL,
        avg_click_depth REAL NOT NULL,
        disallowed_paths_count INTEGER NOT NULL,
        crawl_traps_detected INTEGER NOT NULL,
        findings_json TEXT NOT NULL,
        recommendations_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 5. Index Bloat Detection
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_index_bloat_audits (
        bloat_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        total_routes_analyzed INTEGER NOT NULL,
        thin_content_count INTEGER NOT NULL,
        duplicate_meta_count INTEGER NOT NULL,
        index_efficiency_ratio REAL NOT NULL,
        pruning_targets_json TEXT NOT NULL,
        recommendations_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 6. Striking-Distance Keyword Intelligence
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_striking_distance_queue (
        queue_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        query TEXT NOT NULL,
        url TEXT NOT NULL,
        current_rank REAL NOT NULL,
        search_volume INTEGER NOT NULL,
        commercial_intent TEXT NOT NULL,
        opportunity_index REAL NOT NULL,
        priority TEXT NOT NULL, -- P0_URGENT, P1_HIGH, P2_MEDIUM
        recommended_action TEXT NOT NULL,
        status TEXT DEFAULT 'PENDING_ACTION',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 7. Passage-Level Answerability Analysis
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_passage_answerability (
        passage_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        url TEXT NOT NULL,
        target_query TEXT NOT NULL,
        passage_text TEXT NOT NULL,
        word_count INTEGER NOT NULL,
        answerability_score REAL NOT NULL,
        entity_first INTEGER NOT NULL,
        factual_density REAL NOT NULL,
        fluff_penalty REAL NOT NULL,
        answerability_gap TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 8. Site Reputation Abuse Monitoring
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_reputation_abuse_audits (
        abuse_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        risk_level TEXT NOT NULL, -- CLEAN, LOW_RISK, MEDIUM_RISK, HIGH_RISK
        unauthorized_routes_count INTEGER NOT NULL,
        outbound_links_audited INTEGER NOT NULL,
        suspicious_outbound_links_count INTEGER NOT NULL,
        toxic_backlink_velocity_alert INTEGER NOT NULL,
        audit_findings_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 9. Entity Salience & Relationship Analysis
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_entity_salience (
        entity_audit_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        url TEXT NOT NULL,
        target_entity TEXT NOT NULL,
        salience_score REAL NOT NULL,
        in_title INTEGER NOT NULL,
        in_h1 INTEGER NOT NULL,
        in_first_100_words INTEGER NOT NULL,
        entity_density REAL NOT NULL,
        rdf_triples_json TEXT NOT NULL,
        fact_verification_status TEXT NOT NULL, -- VERIFIED_TRUE, UNVERIFIED, CONTRADICTED
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 10. Generative Engine Optimization (GEO) Measurement
    cur.execute("""
    CREATE TABLE IF NOT EXISTS search_geo_measurements (
        geo_id TEXT PRIMARY KEY,
        provenance_id TEXT NOT NULL,
        query TEXT NOT NULL,
        target_market TEXT NOT NULL,
        ai_overview_present INTEGER NOT NULL,
        suntec_cited INTEGER NOT NULL,
        suntec_citation_url TEXT,
        suntec_ai_voice_share REAL NOT NULL,
        competitors_cited_json TEXT NOT NULL,
        ai_overview_snippet TEXT,
        optimization_advice TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()



def seed_ground_truth_facts():
    """Seeds verified ground-truth metallurgical and corporate facts into Level 1 Memory."""
    facts = [
        ("FACT_CORP_001", "ENTITY", "Legal Corporate Name", "SUNTEC ENTERPRISES", "Corporate Registration (Since 2001)"),
        ("FACT_CORP_002", "ENTITY", "Founding Year", "2001", "Master Knowledge Bank"),
        ("FACT_CORP_003", "FACILITY", "Plant & Office Address", "Sector 49, Faridabad, Haryana 121004, India (Plus Code: 97PC+MP)", "Verified Geo Schema / Google Maps Place MID"),
        ("FACT_CORP_004", "STANDARD", "Quality Management System", "ISO 9001:2015 Certified", "ISO Certificate Registry"),
        ("FACT_CORP_005", "POLICY", "Business Model", "Direct Industrial Manufacturer & Exporter of Cut Wire Shot (Not a trader)", "Executive Directives"),
        ("FACT_CORP_006", "FACILITY", "Production Capacity", "Monthly production capacity exceeding 500 MT of Cut Wire Shot across all alloys", "Knowledge Bank / Plant Audit"),
        
        # Metallurgy & Alloys
        ("FACT_MET_001", "METALLURGY", "Stainless Steel Grades", "SUS 304 (Austenitic, Non-Magnetic/Low-Magnetic, Cr 18-20%, Ni 8-10.5%), SUS 316 (Marine/Chemical, Mo 2-3%), SUS 430 (Ferritic), SUS 202", "ASTM A580 / SAE J441"),
        ("FACT_MET_002", "METALLURGY", "Carbon Steel Cut Wire Hardness", "High Carbon: 45-50 HRC / 50-55 HRC / 55-60 HRC; Regular Carbon: 40-45 HRC", "SAE J441 Specification"),
        ("FACT_MET_003", "METALLURGY", "Conditioning Levels", "As-Cut (Cylindrical with sharp shear edges), Conditioned G1 (Corner-rounded), Conditioned G2 (Double-conditioned, semi-spherical), Conditioned G3 (Fully spherical)", "SAE AMS 2431 & SAE J441"),
        ("FACT_MET_004", "METALLURGY", "Zinc Cut Wire Shot", "Zn >= 99.995%, Density ~7.1 g/cm3, Soft deburring without substrate erosion or spark risk", "DIN 8201 / Lab Tests"),
        ("FACT_MET_005", "METALLURGY", "Copper & Brass Cut Wire Shot", "Cu >= 99.9%, Non-sparking cleaning of electrical contacts, moulds, and architectural brass", "IS 5873"),
        ("FACT_MET_006", "METALLURGY", "Aluminium Cut Wire Shot", "High purity Al, ideal for aluminum die castings to prevent dark staining and iron cross-contamination", "AMS 2431/6"),
        ("FACT_MET_007", "METALLURGY", "Nickel Cut Wire Shot", "High temperature oxidation resistant peening media for jet engine turbine blades and nuclear assemblies", "AMS 2431/8"),

        # Standards Compliance
        ("FACT_STD_001", "STANDARD", "SAE J441", "Standard Specification for Cut Wire Shot", "SAE International"),
        ("FACT_STD_002", "STANDARD", "SAE AMS 2431 Family", "Aerospace Material Specification for Peening Media (AMS 2431/3 Conditioned Carbon, AMS 2431/8 Conditioned Stainless)", "SAE AMS Committee"),
        ("FACT_STD_003", "STANDARD", "DIN 8201-4", "German standard for metallic blast cleaning abrasives (Drahtkorn)", "Deutsches Institut für Normung"),
        ("FACT_STD_004", "STANDARD", "VDFI 8001", "German Spring Manufacturers Association Standard for Spring Peening Media (Drahtkorn für Federherstellung)", "Verband der Deutschen Federnindustrie"),
        ("FACT_STD_005", "STANDARD", "MIL-S-851D", "Military Specification for Metallic Abrasives", "US Department of Defense"),
        ("FACT_STD_006", "STANDARD", "IS 5873-1970", "Indian Standard Specification for Steel Cut Wire Shot", "Bureau of Indian Standards"),
        ("FACT_STD_007", "STANDARD", "EN 10204 3.1", "Inspection Certificate 3.1 provided with all export batches verifying chemical analysis and hardness test results", "European Standard"),
    ]

    conn = get_db()
    cur = conn.cursor()
    for fact in facts:
        cur.execute("""
        INSERT OR REPLACE INTO strategic_facts (fact_id, category, subject, fact_value, verification_source, immutable)
        VALUES (?, ?, ?, ?, ?, 1)
        """, fact)
    conn.commit()
    conn.close()
    print(f"[Strategic Memory] Seeded {len(facts)} Level 1 Ground-Truth Facts.")


def seed_initial_strategic_rules():
    """Seeds proven Level 4 Strategic Rules into Memory."""
    rules = [
        ("RULE_001", "FOUNDATIONAL_101_HEADLINES", "Search intent = Foundational / Educational / Product Overview", "Apply '101' headline framing: '[Topic] 101: Sizes, Applications, Specifications & Selection Guide'. Proven to maximize CTR on broad search queries.", "cut-wire-shot, stainless-steel-cut-wire"),
        ("RULE_002", "STANDARDS_TECHNICAL_HEADLINES", "Search intent = Rigorous Aerospace / Automotive Standards (AMS, VDFI, DIN)", "Apply formal engineering framing: '[Standard ID] Specification Guide: [Component] Shot Peening Standards'. Never use '101' framing for quality engineers or auditors.", "ams-2431, vdfi-8001"),
        ("RULE_003", "AEO_DIRECT_ANSWER_FIRST_PARAGRAPH", "All technical guides and product pages", "Place an exact 2-sentence direct answer definition in the opening hero section before H2 breakdown. Crucial for AI citation extractability.", "all-editorial-content"),
        ("RULE_004", "NO_RAW_PRICING_ON_HIGH_VOLUME_PAGES", "All high-volume transactional queries", "Never display fixed per-kg retail pricing on standard pages; route procurement users directly to certified enterprise RFQ workflows.", "commercial-inquiries")
    ]
    conn = get_db()
    cur = conn.cursor()
    for rule in rules:
        cur.execute("""
        INSERT OR REPLACE INTO strategic_rules (rule_id, rule_name, condition_scope, directive, validation_clusters)
        VALUES (?, ?, ?, ?, ?)
        """, rule)
    conn.commit()
    conn.close()
    print(f"[Strategic Memory] Seeded {len(rules)} Level 4 Strategic Rules.")


def add_observation(obs_id, provenance_id, source, metric_name, metric_value, query, url, evidence_level="MEASURED", confidence="HIGH", metadata=None):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    INSERT OR REPLACE INTO strategic_observations (obs_id, provenance_id, source, metric_name, metric_value, query, url, evidence_level, confidence, observed_at, metadata_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        obs_id, provenance_id, source, metric_name, metric_value, query, url,
        evidence_level, confidence, datetime.utcnow().isoformat() + "Z",
        json.dumps(metadata or {})
    ))
    conn.commit()
    conn.close()


def record_rejection(rejection_id, topic, proposed_query, rejected_by, rejection_category, rationale, review_after_date=None):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    INSERT OR REPLACE INTO strategic_rejections (rejection_id, topic, proposed_query, rejected_by, rejection_category, rationale, review_after_date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (rejection_id, topic, proposed_query, rejected_by, rejection_category, rationale, review_after_date))
    conn.commit()
    conn.close()


def save_opportunity_card(card: dict):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    INSERT OR REPLACE INTO content_opportunity_cards (
        opportunity_id, topic, primary_query, search_intent, buyer_intent, commercial_value,
        current_suntec_page, current_ranking, current_impressions_28d, current_ctr, recommended_action, card_json
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        card["opportunity_id"], card["topic"], card["primary_query"], card["search_intent"], card["buyer_intent"],
        card["commercial_value"], card.get("current_suntec_page"), card.get("current_ranking"),
        card.get("current_impressions_28d", 0), card.get("current_ctr", 0.0), card["recommended_action"],
        json.dumps(card, indent=2)
    ))
    conn.commit()
    conn.close()


def register_experiment(exp: dict):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    INSERT OR REPLACE INTO experiments_registry (
        experiment_id, title, target_url, test_type, hypothesis, status, baseline_json, intervention_json, results_json
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        exp["experiment_id"], exp["title"], exp["target_url"], exp["test_type"], exp["hypothesis"],
        exp["status"], json.dumps(exp.get("baseline_window", {})), json.dumps(exp.get("intervention", {})),
        json.dumps(exp.get("outcome", {}))
    ))
    conn.commit()
    conn.close()


def register_forecast(fc: dict):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    INSERT OR REPLACE INTO forecasts_registry (
        forecast_id, target_query, target_url, target_market, baseline_position,
        p10_weeks, p50_weeks, p90_weeks, confidence, prerequisites_json, forecast_json
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        fc["forecast_id"], fc["target_query"], fc["target_url"], fc["target_market"],
        fc.get("baseline_position"), fc["predictions"]["page_one_visibility"]["p10_weeks"],
        fc["predictions"]["page_one_visibility"]["p50_weeks"], fc["predictions"]["page_one_visibility"]["p90_weeks"],
        fc["predictions"]["page_one_visibility"]["confidence"], json.dumps(fc.get("prerequisites", [])),
        json.dumps(fc, indent=2)
    ))
    conn.commit()
    conn.close()


def export_d1_migration_sql():
    """Generates D1 SQL migration statements to keep Cloudflare D1 synchronized."""
    sql_path = os.path.join(DATA_DIR, "d1_strategic_memory_migration.sql")
    conn = get_db()
    with open(sql_path, "w", encoding="utf-8") as f:
        for line in conn.iterdump():
            if "strategic_" in line or "content_opportunity_" in line or "experiments_" in line or "forecasts_" in line:
                f.write(f"{line}\n")
    conn.close()
    return sql_path


if __name__ == "__main__":
    init_schema()
    seed_ground_truth_facts()
    seed_initial_strategic_rules()
    migration_file = export_d1_migration_sql()
    print(f"[Strategic Memory] Initialized schema and seeded database successfully.")
    print(f"[Strategic Memory] D1 Migration SQL generated: {migration_file}")

CREATE TABLE content_opportunity_cards (
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
INSERT INTO "content_opportunity_cards" VALUES('OPP_20261004_cut_wire_shot','Cut Wire Shot','cut wire shot','INFORMATIONAL_FOUNDATIONAL','DESIGN_ENGINEER',80.0,'/products/cut-wire-shot',8.7,2400,0.017,'UPDATE_EXISTING','{
  "opportunity_id": "OPP_20261004_cut_wire_shot",
  "topic": "Cut Wire Shot",
  "primary_query": "cut wire shot",
  "secondary_queries": [
    "cut wire shot sizes",
    "cut wire shot specification",
    "cut wire shot manufacturer India",
    "cut wire shot price",
    "cut wire shot for shot peening"
  ],
  "search_intent": "INFORMATIONAL_FOUNDATIONAL",
  "buyer_intent": "DESIGN_ENGINEER",
  "commercial_value": 80.0,
  "current_suntec_page": "/products/cut-wire-shot",
  "current_ranking": 8.7,
  "current_impressions_28d": 2400,
  "current_ctr": 0.017,
  "current_traffic_28d": 40,
  "current_conversion_rfq_contribution": 1,
  "serp_format": "TECHNICAL_PILLAR",
  "top_competitors": [
    {
      "domain": "rotocastgroup.com",
      "url": "https://rotocastgroup.com/product-category/cut-wire-shot/",
      "title": "Cut Wire Shots",
      "rank": 1
    },
    {
      "domain": "dir.indiamart.com",
      "url": "https://dir.indiamart.com/impcat/cut-wire-shot.html",
      "title": "Wire Cut Shot Latest Price, Manufacturers & Suppliers",
      "rank": 2
    },
    {
      "domain": "www.airoshotblast.in",
      "url": "https://www.airoshotblast.in/abrasive/cut-wire-shot",
      "title": "Cut Wire Shot - Cut Wire Shots Manufacturer in India at low price",
      "rank": 3
    },
    {
      "domain": "www.allabrasive.com",
      "url": "https://www.allabrasive.com/cut-wire-shot.html",
      "title": "Cut Wire Shot - Steel Shot Trader",
      "rank": 4
    },
    {
      "domain": "suil.in",
      "url": "https://suil.in/products/steel-cut-wire-shots",
      "title": "Steel Cut Wire Shots",
      "rank": 5
    }
  ],
  "competitor_content_patterns": [
    "TECHNICAL_SPECIFICATION",
    "PRICE_COMMERCIAL"
  ],
  "paa_questions": [
    "What is the price of cut wire shot?",
    "What is wire cut?",
    "What is used to cut a wire?",
    "How to cut wire easily?"
  ],
  "related_searches": [
    "cut wire shot grades",
    "cut wire shot suppliers",
    "cut wire shot hrc hardness"
  ],
  "missing_questions": [
    "What is wire cut?",
    "What is used to cut a wire?",
    "How to cut wire easily?"
  ],
  "missing_entities": [
    "SAE J441",
    "Rockwell C Hardness",
    "AMS 2431/8",
    "Austenitic Stainless Steel",
    "Almen Strip Intensity"
  ],
  "missing_evidence": [
    "Ervin durability cycle test data",
    "EN 10204 3.1 mill test certification breakdown"
  ],
  "missing_expertise": [
    "Real plant macro photography of G1/G2/G3 conditioning stages"
  ],
  "headline_patterns": [
    "TECHNICAL_SPECIFICATION",
    "PRICE_COMMERCIAL"
  ],
  "recommended_headline": "Cut Wire Shot 101: Sizes, Applications, Specifications & Selection Guide",
  "recommended_page_format": "TECHNICAL_PILLAR",
  "recommended_h1": "Cut Wire Shot: The Complete Industrial Engineering & Selection Guide",
  "recommended_h2s": [
    "What Is Cut Wire Shot?",
    "Manufacturing Process: Cold Drawn Wire Shearing to Conditioning",
    "Conditioning Grades: As-Cut vs G1, G2, and G3 Spherical",
    "Chemical Composition & Hardness Ranges (SAE J441 / AMS 2431)",
    "Standard Sizing Chart: Diameter & Tolerance Specifications",
    "Industrial Applications: Shot Peening vs Heavy Descaling",
    "Frequently Asked Questions (FAQ)"
  ],
  "recommended_h3s": [
    "SUS 304 vs SUS 316 Chemical Composition",
    "Hardness Testing via Micro-Vickers & HRC Conversion",
    "Conditioning Process: Edge Rounding for Aerospace Peening"
  ],
  "internal_links": [
    {
      "target_url": "/products/stainless-steel-cut-wire-shot",
      "anchor_text": "stainless steel cut wire shot",
      "context": "Product family hub"
    },
    {
      "target_url": "/applications/shot-peening",
      "anchor_text": "aerospace shot peening",
      "context": "Application authority"
    },
    {
      "target_url": "/blog/cut-wire-shot-vs-cast-steel-shot",
      "anchor_text": "cut wire shot vs cast steel shot",
      "context": "Comparison guide"
    }
  ],
  "external_authority_opportunities": [
    "SAE International Standards Portal",
    "VDFI German Spring Manufacturers Association",
    "International Council on Shot Peening (ICSP)"
  ],
  "ai_answer_opportunities": [
    "Concise 2-sentence definition answering: ''What is Cut Wire Shot?''",
    "Direct comparison table answering: ''How does Cut Wire Shot compare to cast steel?''"
  ],
  "risk_of_cannibalization": "LOW",
  "estimated_effort_hours": 6,
  "estimated_impact_score": 85,
  "forecast_summary": "Top 10 expected within 8-14 weeks; page-one commercial capture plausible with internal link reinforcement.",
  "confidence": "HIGH",
  "recommended_action": "UPDATE_EXISTING",
  "reason_not_to_pursue": null
}','2026-10-04 08:19:48');
CREATE TABLE experiments_registry (
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
INSERT INTO "experiments_registry" VALUES('EXP_2026_ut_wire_shot','Headline CTR & AEO Enhancement: Cut Wire Shot','https://suntecenterprises.com/products/cut-wire-shot','HEADLINE_CTR','Deploying the ''101'' foundational headline archetype paired with a 2-sentence AEO definition callout will increase GSC CTR from 1.7% to >= 3.2% within 28 days without loss of impression volume.','APPROVED','{"start_date": "2026-09-06", "end_date": "2026-10-03", "impressions": 2400, "clicks": 41, "ctr": 0.017, "avg_position": 8.7, "ga4_rfqs": 1}','{"applied_date": "2026-10-04", "description": "Update meta title to ''Cut Wire Shot 101: Sizes, Applications, Specifications & Selection Guide'' and insert structured AEO direct-answer block answering ''What is Cut Wire Shot?''", "git_commit_hash": "PENDING_MECHANIC", "human_approved_by": "Human Growth Director (APPROVAL_QUEUE.md)"}','{"status": "ACTIVE_MEASURING", "delta_ctr": null, "delta_position": null, "delta_rfqs": null, "attributed_learning": null}','2026-10-04 08:19:48');
CREATE TABLE forecasts_registry (
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
INSERT INTO "forecasts_registry" VALUES('FC_20261004_ut_wire_shot','cut wire shot','/products/cut-wire-shot','IN',8.7,16,8,4,'HIGH','[{"category": "CONTENT_DEPTH", "requirement": "Incorporate certified SAE J441 and AMS 2431 specification tables into page body", "completed": true}, {"category": "AEO_EXTRACTION", "requirement": "Insert 2-sentence direct answer callout answering ''What is Cut Wire Shot?'' in hero block", "completed": false}, {"category": "INTERNAL_LINKS", "requirement": "Establish 3 inbound contextual links from application pages (/applications/shot-peening)", "completed": true}, {"category": "AUTHORITY", "requirement": "Verify EN 10204 3.1 inspection certification badge on page", "completed": false}]','{
  "forecast_id": "FC_20261004_ut_wire_shot",
  "opportunity_id": "OPP_20261004_cut_wire_shot",
  "generated_date": "2026-10-04T08:19:48.609580Z",
  "target_query": "cut wire shot",
  "target_url": "/products/cut-wire-shot",
  "target_market": "IN",
  "baseline_position": 8.7,
  "predictions": {
    "page_one_visibility": {
      "p90_weeks": 4,
      "p50_weeks": 8,
      "p10_weeks": 16,
      "confidence": "HIGH"
    },
    "top_three_visibility": {
      "p90_months": 2,
      "p50_months": 4,
      "p10_months": 8,
      "confidence": "MEDIUM"
    },
    "monthly_traffic_gain_p50": 84,
    "monthly_rfq_gain_p50": 3,
    "attributed_revenue_potential_p50": "\u20b91,050,000 - \u20b92,400,000"
  },
  "prerequisites": [
    {
      "category": "CONTENT_DEPTH",
      "requirement": "Incorporate certified SAE J441 and AMS 2431 specification tables into page body",
      "completed": true
    },
    {
      "category": "AEO_EXTRACTION",
      "requirement": "Insert 2-sentence direct answer callout answering ''What is Cut Wire Shot?'' in hero block",
      "completed": false
    },
    {
      "category": "INTERNAL_LINKS",
      "requirement": "Establish 3 inbound contextual links from application pages (/applications/shot-peening)",
      "completed": true
    },
    {
      "category": "AUTHORITY",
      "requirement": "Verify EN 10204 3.1 inspection certification badge on page",
      "completed": false
    }
  ],
  "acceleration_factors": [
    "Fast Google re-crawl via IndexNow multi-engine ping",
    "Direct quote form CTA above the fold on mobile viewports",
    "High commercial CTR hook in meta description"
  ],
  "delay_factors": [
    "Entrenched directory aggregators (IndiaMART, Justdial) dominating generic transactional queries",
    "Competitor content refresh by international abrasive manufacturers",
    "Search algorithm core updates shifting informational/transactional intent ratios"
  ],
  "assumptions": [
    "Website Core Web Vitals remain in Google ''Good'' threshold",
    "Zero 4xx/5xx crawl errors on target URL",
    "Strict white-hat compliance (zero artificial link schemes)"
  ]
}','2026-10-04 08:19:48');
CREATE TABLE strategic_facts (
        fact_id TEXT PRIMARY KEY,
        category TEXT NOT NULL, -- ENTITY, METALLURGY, STANDARD, FACILITY, POLICY
        subject TEXT NOT NULL,
        fact_value TEXT NOT NULL,
        verification_source TEXT NOT NULL,
        immutable INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "strategic_facts" VALUES('FACT_CORP_001','ENTITY','Legal Corporate Name','SUNTEC ENTERPRISES','Corporate Registration (Since 2001)',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_CORP_002','ENTITY','Founding Year','2001','Master Knowledge Bank',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_CORP_003','FACILITY','Plant & Office Address','Sector 49, Faridabad, Haryana 121004, India (Plus Code: 97PC+MP)','Verified Geo Schema / Google Maps Place MID',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_CORP_004','STANDARD','Quality Management System','ISO 9001:2015 Certified','ISO Certificate Registry',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_CORP_005','POLICY','Business Model','Direct Industrial Manufacturer & Exporter of Cut Wire Shot (Not a trader)','Executive Directives',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_CORP_006','FACILITY','Production Capacity','Monthly production capacity exceeding 500 MT of Cut Wire Shot across all alloys','Knowledge Bank / Plant Audit',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_MET_001','METALLURGY','Stainless Steel Grades','SUS 304 (Austenitic, Non-Magnetic/Low-Magnetic, Cr 18-20%, Ni 8-10.5%), SUS 316 (Marine/Chemical, Mo 2-3%), SUS 430 (Ferritic), SUS 202','ASTM A580 / SAE J441',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_MET_002','METALLURGY','Carbon Steel Cut Wire Hardness','High Carbon: 45-50 HRC / 50-55 HRC / 55-60 HRC; Regular Carbon: 40-45 HRC','SAE J441 Specification',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_MET_003','METALLURGY','Conditioning Levels','As-Cut (Cylindrical with sharp shear edges), Conditioned G1 (Corner-rounded), Conditioned G2 (Double-conditioned, semi-spherical), Conditioned G3 (Fully spherical)','SAE AMS 2431 & SAE J441',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_MET_004','METALLURGY','Zinc Cut Wire Shot','Zn >= 99.995%, Density ~7.1 g/cm3, Soft deburring without substrate erosion or spark risk','DIN 8201 / Lab Tests',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_MET_005','METALLURGY','Copper & Brass Cut Wire Shot','Cu >= 99.9%, Non-sparking cleaning of electrical contacts, moulds, and architectural brass','IS 5873',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_MET_006','METALLURGY','Aluminium Cut Wire Shot','High purity Al, ideal for aluminum die castings to prevent dark staining and iron cross-contamination','AMS 2431/6',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_MET_007','METALLURGY','Nickel Cut Wire Shot','High temperature oxidation resistant peening media for jet engine turbine blades and nuclear assemblies','AMS 2431/8',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_STD_001','STANDARD','SAE J441','Standard Specification for Cut Wire Shot','SAE International',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_STD_002','STANDARD','SAE AMS 2431 Family','Aerospace Material Specification for Peening Media (AMS 2431/3 Conditioned Carbon, AMS 2431/8 Conditioned Stainless)','SAE AMS Committee',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_STD_003','STANDARD','DIN 8201-4','German standard for metallic blast cleaning abrasives (Drahtkorn)','Deutsches Institut für Normung',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_STD_004','STANDARD','VDFI 8001','German Spring Manufacturers Association Standard for Spring Peening Media (Drahtkorn für Federherstellung)','Verband der Deutschen Federnindustrie',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_STD_005','STANDARD','MIL-S-851D','Military Specification for Metallic Abrasives','US Department of Defense',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_STD_006','STANDARD','IS 5873-1970','Indian Standard Specification for Steel Cut Wire Shot','Bureau of Indian Standards',1,'2026-10-04 08:17:45');
INSERT INTO "strategic_facts" VALUES('FACT_STD_007','STANDARD','EN 10204 3.1','Inspection Certificate 3.1 provided with all export batches verifying chemical analysis and hardness test results','European Standard',1,'2026-10-04 08:17:45');
CREATE TABLE strategic_learnings (
        learning_id TEXT PRIMARY KEY,
        experiment_id TEXT,
        topic_cluster TEXT NOT NULL,
        learning_statement TEXT NOT NULL,
        supporting_evidence TEXT NOT NULL,
        confidence TEXT NOT NULL, -- HIGH, MEDIUM, LOW
        promoted_from_obs_count INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE strategic_observations (
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
INSERT INTO "strategic_observations" VALUES('OBS_SERP_1791082188','prov_serp_d22c607d7974','DATAFORSEO_LIVE_SERP','serp_organic_count',7.0,'cut wire shot','https://suntecenterprises.com/products/cut-wire-shot','OBSERVED','HIGH','2026-10-04T08:19:48.606349Z','{"paa_count": 4, "ai_overview": true}');
CREATE TABLE strategic_rejections (
        rejection_id TEXT PRIMARY KEY,
        topic TEXT NOT NULL,
        proposed_query TEXT NOT NULL,
        rejected_by TEXT NOT NULL,
        rejection_category TEXT NOT NULL,
        rationale TEXT NOT NULL,
        review_after_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE strategic_rules (
        rule_id TEXT PRIMARY KEY,
        rule_name TEXT NOT NULL,
        condition_scope TEXT NOT NULL,
        directive TEXT NOT NULL,
        validation_clusters TEXT NOT NULL, -- e.g. "foundational, comparisons"
        status TEXT DEFAULT 'ACTIVE', -- ACTIVE, UNDER_INVESTIGATION, DEPRECATED
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "strategic_rules" VALUES('RULE_001','FOUNDATIONAL_101_HEADLINES','Search intent = Foundational / Educational / Product Overview','Apply ''101'' headline framing: ''[Topic] 101: Sizes, Applications, Specifications & Selection Guide''. Proven to maximize CTR on broad search queries.','cut-wire-shot, stainless-steel-cut-wire','ACTIVE','2026-10-04 08:17:45');
INSERT INTO "strategic_rules" VALUES('RULE_002','STANDARDS_TECHNICAL_HEADLINES','Search intent = Rigorous Aerospace / Automotive Standards (AMS, VDFI, DIN)','Apply formal engineering framing: ''[Standard ID] Specification Guide: [Component] Shot Peening Standards''. Never use ''101'' framing for quality engineers or auditors.','ams-2431, vdfi-8001','ACTIVE','2026-10-04 08:17:45');
INSERT INTO "strategic_rules" VALUES('RULE_003','AEO_DIRECT_ANSWER_FIRST_PARAGRAPH','All technical guides and product pages','Place an exact 2-sentence direct answer definition in the opening hero section before H2 breakdown. Crucial for AI citation extractability.','all-editorial-content','ACTIVE','2026-10-04 08:17:45');
INSERT INTO "strategic_rules" VALUES('RULE_004','NO_RAW_PRICING_ON_HIGH_VOLUME_PAGES','All high-volume transactional queries','Never display fixed per-kg retail pricing on standard pages; route procurement users directly to certified enterprise RFQ workflows.','commercial-inquiries','ACTIVE','2026-10-04 08:17:45');

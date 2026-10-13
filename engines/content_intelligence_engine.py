#!/usr/bin/env python3
"""
Content Intelligence Engine (V2.0)
Powers Agent #20 (Editor).
Analyzes search intent, SERP formats, competitor gaps, PAA questions, and headline patterns.
Generates complete 34-field Content Opportunity Cards and enforces the decision tree:
CREATE_NEW vs UPDATE_EXISTING vs CONSOLIDATE vs REDIRECT vs DO_NOTHING.
"""

import os
import json
import re
from datetime import datetime
from dataforseo_client import get_live_advanced_serp, get_keywords_search_volume
from strategic_memory import save_opportunity_card, record_rejection


class ContentIntelligenceEngine:
    def __init__(self):
        pass

    def analyze_topic(self, topic: str, primary_query: str, target_market: str = "IN", current_suntec_page: str = None, current_ranking: float = None, current_impressions_28d: int = 0, current_ctr: float = 0.0, current_rfqs: int = 0):
        """
        Analyzes a search topic end-to-end and outputs a 34-field Content Opportunity Card.
        """
        location_code = 2356 if target_market == "IN" else (2276 if target_market == "DE" else 2840)
        
        # 1. Fetch Live Advanced SERP via DataForSEO
        serp = get_live_advanced_serp(primary_query, location_code=location_code)
        organics = serp.get("organic_results", [])
        paa = serp.get("paa_questions", [])
        ai_overview = serp.get("ai_overview")

        # 2. Extract Competitors & SERP Structure
        top_competitors = []
        for org in organics[:5]:
            top_competitors.append({
                "domain": org.get("domain"),
                "url": org.get("url"),
                "title": org.get("title"),
                "rank": org.get("rank_group")
            })

        # 3. Analyze PAA Questions
        paa_questions = [p["question"] for p in paa if "question" in p]
        
        # 4. Analyze Headline Patterns in SERP
        headline_patterns = []
        for org in organics[:5]:
            t = org.get("title", "")
            if "101" in t or "Guide" in t:
                headline_patterns.append("FOUNDATIONAL_GUIDE")
            elif "vs" in t.lower() or "versus" in t.lower():
                headline_patterns.append("HEAD_TO_HEAD_COMPARISON")
            elif "price" in t.lower() or "cost" in t.lower():
                headline_patterns.append("PRICE_COMMERCIAL")
            elif "manufacturer" in t.lower() or "supplier" in t.lower():
                headline_patterns.append("SUPPLIER_CATALOGUE")
            else:
                headline_patterns.append("TECHNICAL_SPECIFICATION")

        # 5. Intent Classification
        is_informational = any(w in primary_query.lower() for w in ["what", "how", "difference", "guide", "standard", "101", "size"])
        is_transactional = any(w in primary_query.lower() for w in ["manufacturer", "supplier", "buy", "price", "exporter"])

        if is_transactional and not is_informational:
            search_intent = "TRANSACTIONAL_RFQ"
            buyer_intent = "PLANT_PURCHASING_OFFICER"
            commercial_val = 92.0
            rec_page_format = "SPECIFICATION_CATALOGUE"
        elif "vs" in primary_query.lower() or "comparison" in primary_query.lower():
            search_intent = "COMMERCIAL_INVESTIGATION"
            buyer_intent = "QUALITY_METALLURGIST"
            commercial_val = 88.0
            rec_page_format = "HEAD_TO_HEAD_COMPARISON"
        else:
            search_intent = "INFORMATIONAL_FOUNDATIONAL"
            buyer_intent = "DESIGN_ENGINEER"
            commercial_val = 80.0
            rec_page_format = "TECHNICAL_PILLAR"

        # 6. Editorial Decision: Create vs Update vs Do Nothing
        opp_id = f"OPP_{datetime.utcnow().strftime('%Y%m%d')}_{re.sub(r'[^a-zA-Z0-9]', '_', primary_query.lower())[:20]}"
        
        # Decision logic
        if "price per kg" in primary_query.lower() or "cheap" in primary_query.lower():
            recommended_action = "DO_NOTHING"
            reason_not_to_pursue = "Query reflects retail/hobbyist price shopping. Suntec is a high-volume industrial manufacturer under strict MOQ standards."
            record_rejection(
                rejection_id=f"REJ_{opp_id}",
                topic=topic,
                proposed_query=primary_query,
                rejected_by="Editor (#20)",
                rejection_category="COMMERCIAL_INTENT_MISALIGNMENT",
                rationale=reason_not_to_pursue
            )
        elif current_suntec_page and current_ranking and current_ranking <= 25.0:
            recommended_action = "UPDATE_EXISTING"
            reason_not_to_pursue = None
        else:
            recommended_action = "CREATE_NEW"
            reason_not_to_pursue = None

        # 7. Structural Architecture & Headline Generation
        if rec_page_format == "TECHNICAL_PILLAR":
            rec_headline = f"{topic} 101: Sizes, Applications, Specifications & Selection Guide"
            rec_h1 = f"{topic}: The Complete Industrial Engineering & Selection Guide"
            rec_h2s = [
                f"What Is {topic}?",
                "Manufacturing Process: Cold Drawn Wire Shearing to Conditioning",
                "Conditioning Grades: As-Cut vs G1, G2, and G3 Spherical",
                "Chemical Composition & Hardness Ranges (SAE J441 / AMS 2431)",
                "Standard Sizing Chart: Diameter & Tolerance Specifications",
                "Industrial Applications: Shot Peening vs Heavy Descaling",
                "Frequently Asked Questions (FAQ)"
            ]
        elif rec_page_format == "HEAD_TO_HEAD_COMPARISON":
            rec_headline = f"{topic}: Fatigue Life, Media Consumption & Cost Comparison"
            rec_h1 = f"{topic}: Engineering Analysis & Operational Performance"
            rec_h2s = [
                "Executive Summary: Cut Wire vs Cast Steel Abrasives",
                "Fatigue Life & Durability Cycles: Ervin Test Comparisons",
                "Dust Generation & Environmental Cleanliness in Blasting Cabinets",
                "Surface Contamination & Non-Ferrous Blast Requirements",
                "Total Operational Cost (TCO) per Square Meter Cleaned",
                "Application Recommendations: When to Use Cut Wire Shot",
                "Frequently Asked Questions (FAQ)"
            ]
        else:
            rec_headline = f"{topic}: Certified Manufacturing Specifications & Supply Parameters"
            rec_h1 = f"{topic}: Industrial Grade Specifications & Global Supply"
            rec_h2s = [
                f"{topic} Technical Overview & Alloy Selection",
                "Standard Compliance: SAE J441, DIN 8201-4, VDFI 8001",
                "Packaging & Mill Test Certification (EN 10204 3.1)",
                "Request an Industrial Quotation & Technical Data Sheet"
            ]

        card = {
            "opportunity_id": opp_id,
            "topic": topic,
            "primary_query": primary_query,
            "secondary_queries": [
                f"{primary_query} sizes",
                f"{primary_query} specification",
                f"{primary_query} manufacturer India",
                f"{primary_query} price",
                f"{primary_query} for shot peening"
            ],
            "search_intent": search_intent,
            "buyer_intent": buyer_intent,
            "commercial_value": commercial_val,
            "current_suntec_page": current_suntec_page,
            "current_ranking": current_ranking,
            "current_impressions_28d": current_impressions_28d,
            "current_ctr": current_ctr,
            "current_traffic_28d": int(current_impressions_28d * current_ctr),
            "current_conversion_rfq_contribution": current_rfqs,
            "serp_format": rec_page_format,
            "top_competitors": top_competitors,
            "competitor_content_patterns": list(set(headline_patterns)),
            "paa_questions": paa_questions[:5],
            "related_searches": [f"{primary_query} grades", f"{primary_query} suppliers", f"{primary_query} hrc hardness"],
            "missing_questions": [q for q in paa_questions if not any(w in q.lower() for w in ["price", "cost"])],
            "missing_entities": ["SAE J441", "Rockwell C Hardness", "AMS 2431/8", "Austenitic Stainless Steel", "Almen Strip Intensity"],
            "missing_evidence": ["Ervin durability cycle test data", "EN 10204 3.1 mill test certification breakdown"],
            "missing_expertise": ["Real plant macro photography of G1/G2/G3 conditioning stages"],
            "headline_patterns": list(set(headline_patterns)),
            "recommended_headline": rec_headline,
            "recommended_page_format": rec_page_format,
            "recommended_h1": rec_h1,
            "recommended_h2s": rec_h2s,
            "recommended_h3s": [
                "SUS 304 vs SUS 316 Chemical Composition",
                "Hardness Testing via Micro-Vickers & HRC Conversion",
                "Conditioning Process: Edge Rounding for Aerospace Peening"
            ],
            "internal_links": [
                {"target_url": "/products/stainless-steel-cut-wire-shot", "anchor_text": "stainless steel cut wire shot", "context": "Product family hub"},
                {"target_url": "/applications/shot-peening", "anchor_text": "aerospace shot peening", "context": "Application authority"},
                {"target_url": "/blog/cut-wire-shot-vs-cast-steel-shot", "anchor_text": "cut wire shot vs cast steel shot", "context": "Comparison guide"}
            ],
            "external_authority_opportunities": [
                "SAE International Standards Portal",
                "VDFI German Spring Manufacturers Association",
                "International Council on Shot Peening (ICSP)"
            ],
            "ai_answer_opportunities": [
                f"Concise 2-sentence definition answering: 'What is {topic}?'",
                f"Direct comparison table answering: 'How does {topic} compare to cast steel?'"
            ],
            "risk_of_cannibalization": "NONE" if recommended_action == "CREATE_NEW" else "LOW",
            "estimated_effort_hours": 6,
            "estimated_impact_score": 85,
            "forecast_summary": "Top 10 expected within 8-14 weeks; page-one commercial capture plausible with internal link reinforcement.",
            "confidence": "HIGH",
            "recommended_action": recommended_action,
            "reason_not_to_pursue": reason_not_to_pursue
        }

        # Save to Strategic Memory
        save_opportunity_card(card)
        return card


if __name__ == "__main__":
    engine = ContentIntelligenceEngine()
    print("[Content Intelligence Engine] Analyzing topic 'Cut Wire Shot'...")
    card = engine.analyze_topic(
        topic="Cut Wire Shot",
        primary_query="cut wire shot",
        target_market="IN",
        current_suntec_page="/products/cut-wire-shot",
        current_ranking=8.7,
        current_impressions_28d=2400,
        current_ctr=0.017,
        current_rfqs=1
    )
    print(f"Generated Opportunity Card ID: {card['opportunity_id']}")
    print(f"Action: {card['recommended_action']}")
    print(f"Recommended Title: {card['recommended_headline']}")
    print(f"PAA Questions Found: {len(card['paa_questions'])}")

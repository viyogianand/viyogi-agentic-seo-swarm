#!/usr/bin/env python3
"""
Unit & Integration Test Suite for Search Intelligence & Technical SEO Autonomy Layer
Suntec Enterprises Growth Swarm
"""

import os
import sys
import json
import unittest
import sqlite3

# Set up environment path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from engines.search_intelligence_engine import (
    QueryFanOutAnalyzer,
    InformationGainAnalyzer,
    CannibalizationDetector,
    CrawlBudgetAuditor,
    IndexBloatDetector,
    StrikingDistanceAnalyzer,
    PassageAnswerabilityAnalyzer,
    ReputationAbuseMonitor,
    EntitySalienceAnalyzer,
    GEOMonitor,
    SearchIntelligenceEngine
)
from engines.strategic_memory import get_db, init_schema


class TestSearchIntelligenceEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_schema()

    def test_01_query_fanout(self):
        analyzer = QueryFanOutAnalyzer()
        res = analyzer.analyze_fanout("cut wire shot", target_market="IN")

        self.assertIn("fanout_id", res)
        self.assertIn("provenance_id", res)
        self.assertEqual(res["seed_query"], "cut wire shot")
        self.assertGreater(res["total_nodes"], 0)
        self.assertGreater(res["modeled_nodes_count"], 0)

        # Check modeled tiers
        tree = res["tree"]
        self.assertIn("modeled_tiers", tree)
        intents = [node["intent"] for node in tree["modeled_tiers"]]
        self.assertIn("COMMERCIAL_SPEC", intents)
        self.assertIn("PROCUREMENT_TRANSACTIONAL", intents)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT seed_query, total_nodes FROM search_query_fanout WHERE fanout_id = ?", (res["fanout_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["seed_query"], "cut wire shot")

    def test_02_information_gain(self):
        analyzer = InformationGainAnalyzer()
        competitor_text = "Cut wire shot is an abrasive. It is used in blasting machines. Contact us for competitive price."
        suntec_text = """
        Suntec Enterprises produces cut wire shot adhering to SAE J441 and AMS 2431.
        Hardness ranges: High Carbon 45-50 HRC and 50-55 HRC.
        Conditioning grades include As-Cut, G1, G2, and G3 spherical media.
        In Ervin fatigue tests, cut wire shot achieves over 3,500 durability cycles compared to 1,800 for cast steel shot.
        Chemical composition: Cr 18-20%, Ni 8-10.5% for SUS 304.
        Mill test certificates comply with EN 10204 3.1.
        | Size | Diameter (mm) | Tolerance (+/- mm) |
        |---|---|---|
        | CW-14 | 0.35 | 0.02 |
        """
        res = analyzer.analyze_information_gain(
            target_query="cut wire shot",
            target_url="https://suntecenterprises.com/blog/cut-wire-shot-101",
            competitor_text=competitor_text,
            suntec_text=suntec_text
        )

        self.assertIn("information_gain_score", res)
        self.assertGreaterEqual(res["information_gain_score"], 70.0)
        self.assertIn("novel_data_score", res["score_breakdown"])
        self.assertGreater(res["score_breakdown"]["novel_data_score"], 15.0)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT information_gain_score FROM search_information_gain WHERE gain_id = ?", (res["gain_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["information_gain_score"], res["information_gain_score"])

    def test_03_keyword_cannibalization(self):
        detector = CannibalizationDetector()
        res = detector.detect_cannibalization(
            query="cut wire shot",
            primary_url="https://suntecenterprises.com/products/cut-wire-shot",
            primary_rank=12.0,
            competing_url="https://suntecenterprises.com/blog/cut-wire-shot-101",
            competing_rank=14.0,
            title_similarity=0.88
        )

        self.assertEqual(res["severity"], "CRITICAL")
        self.assertEqual(res["recommended_action"], "CANONICAL_CONSOLIDATION")
        self.assertEqual(res["approval_status"], "PENDING_HUMAN_APPROVAL")

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT severity, recommended_action FROM search_cannibalization_findings WHERE finding_id = ?", (res["finding_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["severity"], "CRITICAL")

    def test_04_crawl_budget(self):
        auditor = CrawlBudgetAuditor()
        res = auditor.audit_crawl_budget()

        self.assertEqual(res["evidence_level"], "SIMULATED_ARCHITECTURAL")
        self.assertIn("STATIC_CODEBASE_ANALYSIS", res["data_source"])
        self.assertLessEqual(res["max_click_depth"], 3)
        self.assertGreaterEqual(res["total_urls_audited"], 10)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT max_click_depth FROM search_crawl_budget_audits WHERE audit_id = ?", (res["audit_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)

    def test_05_index_bloat(self):
        detector = IndexBloatDetector()
        res = detector.detect_index_bloat()

        self.assertIn("index_efficiency_ratio", res)
        self.assertGreaterEqual(res["index_efficiency_ratio"], 70.0)
        self.assertIsInstance(res["pruning_targets"], list)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT index_efficiency_ratio FROM search_index_bloat_audits WHERE bloat_id = ?", (res["bloat_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)

    def test_06_striking_distance(self):
        analyzer = StrikingDistanceAnalyzer()
        res = analyzer.analyze_striking_distance()

        self.assertIsInstance(res, list)
        self.assertGreater(len(res), 0)
        for item in res:
            # Must strictly be within positions 4.0 to 20.0
            self.assertGreaterEqual(item["current_rank"], 4.0)
            self.assertLessEqual(item["current_rank"], 20.0)
            self.assertGreater(item["opportunity_index"], 0.0)
            self.assertIn("priority", item)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM search_striking_distance_queue")
        cnt = cur.fetchone()[0]
        conn.close()
        self.assertGreaterEqual(cnt, len(res))

    def test_07_passage_answerability(self):
        analyzer = PassageAnswerabilityAnalyzer()
        text = """
        Cut wire shot is an industrial abrasive manufactured by cold drawing steel wire and shearing it into cylindrical pellets.
        Hardness ranges between 45 to 55 HRC adhering to SAE J441 and AMS 2431 standards with precise diameter tolerances.
        
        Welcome to our website! In this article we will delve into exciting topics and explore many general abrasive things.
        """
        res = analyzer.analyze_passages(
            url="https://suntecenterprises.com/blog/cut-wire-shot-101",
            text_content=text,
            target_paa_query="What is cut wire shot?"
        )

        self.assertGreaterEqual(res["passages_count"], 2)
        self.assertGreaterEqual(res["highest_passage_score"], 70.0)
        # First passage has entity first and high factual density
        first_passage = res["passages"][0]
        self.assertTrue(first_passage["entity_first"])

        # Second passage has fluff penalty
        second_passage = res["passages"][1]
        self.assertGreater(second_passage["fluff_penalty"], 0.0)

    def test_08_reputation_abuse(self):
        monitor = ReputationAbuseMonitor()
        res = monitor.monitor_reputation_abuse()

        self.assertEqual(res["risk_level"], "CLEAN")
        self.assertEqual(res["unauthorized_routes_count"], 0)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT risk_level FROM search_reputation_abuse_audits WHERE abuse_id = ?", (res["abuse_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["risk_level"], "CLEAN")

    def test_09_entity_salience(self):
        analyzer = EntitySalienceAnalyzer()
        content = """
        Suntec Enterprises manufactures premium Cut Wire Shot in Faridabad, India.
        Our cut wire shot strictly complies with SAE J441 and AMS 2431 for shot peening.
        """
        res = analyzer.analyze_entity_salience(
            url="https://suntecenterprises.com/products/cut-wire-shot",
            page_title="Cut Wire Shot Manufacturer | Suntec Enterprises",
            page_h1="Cut Wire Shot Specifications",
            content_text=content,
            target_entity="Cut Wire Shot"
        )

        self.assertGreaterEqual(res["salience_score"], 65.0)
        self.assertTrue(res["in_title"])
        self.assertTrue(res["in_h1"])
        self.assertGreater(len(res["rdf_triples"]), 2)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT salience_score FROM search_entity_salience WHERE entity_audit_id = ?", (res["entity_audit_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)

    def test_10_geo_measurement(self):
        monitor = GEOMonitor()
        res = monitor.measure_geo_visibility("cut wire shot", target_market="IN")

        self.assertIn("ai_overview_present", res)
        self.assertIn("suntec_cited", res)
        self.assertIn("suntec_ai_voice_share", res)
        self.assertIn("competitors_cited", res)
        self.assertIn("optimization_advice", res)

        # Verify SQLite insertion
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT query FROM search_geo_measurements WHERE geo_id = ?", (res["geo_id"],))
        row = cur.fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["query"], "cut wire shot")

    def test_11_full_swarm_orchestration(self):
        engine = SearchIntelligenceEngine()
        result = engine.run_full_search_intelligence_cycle("cut wire shot", "IN")

        self.assertEqual(result["execution_status"], "SUCCESS")
        self.assertEqual(len(result["capabilities"]), 10)
        self.assertGreater(result["elapsed_seconds"], 0.0)


if __name__ == "__main__":
    unittest.main()

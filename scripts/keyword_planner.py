#!/usr/bin/env python3
"""
Vivaak — Google Keyword Planner & Search Volume Tool
Powered by DataForSEO API
"""

import sys
import json
import urllib.request
import argparse

API_LOGIN = "info@suntecenterprises.com"
API_PASSWORD = "535fd6e71898eb6e"
AUTH_HEADER = "Basic aW5mb0BzdW50ZWNlbnRlcnByaXNlcy5jb206NTM1ZmQ2ZTcxODk4ZWI2ZQ=="

def get_keyword_ideas(keywords, location_code=2356, language_code="en", limit=50):
    """
    Query Google Keyword Planner for related keywords, search volumes, competition, and CPC.
    Location code 2356 = India.
    """
    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/keywords_for_keywords/live"
    post_data = [{
        "keywords": keywords if isinstance(keywords, list) else [keywords],
        "location_code": location_code,
        "language_code": language_code
    }]

    req = urllib.request.Request(
        url,
        data=json.dumps(post_data).encode("utf-8"),
        headers={
            "Authorization": AUTH_HEADER,
            "Content-Type": "application/json"
        }
    )

    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    if res.get("status_code") != 20000:
        raise RuntimeError(f"DataForSEO error {res.get('status_code')}: {res.get('status_message')}")

    results = res["tasks"][0]["result"] or []
    return results[:limit]

def get_search_volume(keywords, location_code=2356, language_code="en"):
    """
    Get exact Google search volume history for specific keywords.
    """
    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
    post_data = [{
        "keywords": keywords if isinstance(keywords, list) else [keywords],
        "location_code": location_code,
        "language_code": language_code
    }]

    req = urllib.request.Request(
        url,
        data=json.dumps(post_data).encode("utf-8"),
        headers={
            "Authorization": AUTH_HEADER,
            "Content-Type": "application/json"
        }
    )

    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    if res.get("status_code") != 20000:
        raise RuntimeError(f"DataForSEO error {res.get('status_code')}: {res.get('status_message')}")

    return res["tasks"][0]["result"] or []

def main():
    parser = argparse.ArgumentParser(description="Vivaak Google Keyword Planner Tool")
    parser.add_argument("keywords", nargs="+", help="Seed keywords to analyze")
    parser.add_argument("--limit", type=int, default=20, help="Number of keyword ideas to display")
    parser.add_argument("--location", type=int, default=2356, help="Location code (default: 2356 for India)")
    args = parser.parse_args()

    print(f"\n🔍 Fetching Google Keyword Planner data for: {', '.join(args.keywords)} (Location: India)...")
    items = get_keyword_ideas(args.keywords, location_code=args.location, limit=args.limit)

    print(f"\n{'Keyword':<45} | {'Monthly Vol':<12} | {'Competition':<12} | {'CPC (USD)':<10}")
    print("-" * 85)
    for item in items:
        kw = item.get("keyword", "")
        vol = item.get("search_volume") or 0
        comp = item.get("competition_level") or "N/A"
        cpc = f"${item.get('cpc'):.2f}" if item.get("cpc") is not None else "N/A"
        print(f"{kw:<45} | {vol:<12} | {comp:<12} | {cpc:<10}")

    print("\n✅ Keyword Planner query completed successfully!\n")

if __name__ == "__main__":
    main()

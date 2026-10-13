#!/usr/bin/env python3
"""
Vivaak & Vaza — Google Search Console Rank & Traffic Tracker
Pulls live search queries, clicks, impressions, CTR, and average position for sc-domain:vivaak.com.
"""

import sys
import json
import urllib.request
import urllib.parse
import os
import argparse
from datetime import datetime, timedelta

CREDS_FILE = os.path.expanduser("~/.gemini/config/google-credentials.json")
SITE_URL = "sc-domain:vivaak.com"

def get_access_token():
    with open(CREDS_FILE, "r") as f:
        creds = json.load(f)

    data = urllib.parse.urlencode({
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "refresh_token": creds["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        tokens = json.loads(resp.read().decode("utf-8"))

    return tokens["access_token"]

def query_search_analytics(dimension="query", days=28, row_limit=25):
    token = get_access_token()
    site_enc = urllib.parse.quote(SITE_URL, safe="")
    url = f"https://www.googleapis.com/webmasters/v3/sites/{site_enc}/searchAnalytics/query"

    end_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days + 2)).strftime("%Y-%m-%d")

    payload = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": [dimension],
        "rowLimit": row_limit
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    return res.get("rows", []), start_date, end_date

def main():
    parser = argparse.ArgumentParser(description="Vivaak Google Search Console Rank Tracker")
    parser.add_argument("--dim", choices=["query", "page", "device", "country"], default="query", help="Dimension to group by")
    parser.add_argument("--days", type=int, default=28, help="Number of past days to query")
    parser.add_argument("--limit", type=int, default=20, help="Number of rows to return")
    args = parser.parse_args()

    print(f"\n📊 Querying Google Search Console for '{SITE_URL}' (Last {args.days} days, grouped by {args.dim})...")
    rows, start, end = query_search_analytics(dimension=args.dim, days=args.days, row_limit=args.limit)

    print(f"Date Range: {start} to {end} | Total Records: {len(rows)}\n")

    if not rows:
        print("ℹ️  No search performance rows returned for this date range yet.")
        return

    print(f"{'Key / ' + args.dim.capitalize():<50} | {'Clicks':<8} | {'Impressions':<12} | {'CTR':<8} | {'Position':<8}")
    print("-" * 95)
    for r in rows:
        key = r.get("keys", [""])[0]
        clicks = r.get("clicks", 0)
        impr = r.get("impressions", 0)
        ctr = f"{r.get('ctr', 0) * 100:.1f}%"
        pos = f"{r.get('position', 0):.1f}"
        print(f"{key:<50} | {clicks:<8} | {impr:<12} | {ctr:<8} | {pos:<8}")
    print("")

if __name__ == "__main__":
    main()

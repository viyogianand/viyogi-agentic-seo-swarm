#!/usr/bin/env python3
"""
Vivaak & Vaza — GA4 Realtime & Traffic Analytics Monitor
Pulls active visitors, country breakdown, traffic channels, and daily sessions for The Vivaak Villa.
"""

import sys
import json
import urllib.request
import urllib.parse
import os
import argparse
from datetime import datetime, timedelta

CREDS_FILE = os.path.expanduser("~/.gemini/config/google-credentials.json")
PROPERTY_ID = "356471972" # The Vivaak Villa

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

def get_realtime_report(token):
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runRealtimeReport"
    payload = {
        "metrics": [{"name": "activeUsers"}],
        "dimensions": [{"name": "country"}, {"name": "city"}]
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
        return json.loads(resp.read().decode("utf-8"))

def get_daily_report(token, days=30):
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"
    payload = {
        "dateRanges": [{"startDate": f"{days}daysAgo", "endDate": "yesterday"}],
        "dimensions": [{"name": "date"}],
        "metrics": [
            {"name": "totalUsers"},
            {"name": "sessions"},
            {"name": "screenPageViews"},
            {"name": "engagementRate"}
        ],
        "orderBys": [{"dimension": {"dimensionName": "date"}, "desc": True}]
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
        return json.loads(resp.read().decode("utf-8"))

def main():
    parser = argparse.ArgumentParser(description="Vivaak GA4 Traffic Monitor")
    parser.add_argument("--days", type=int, default=14, help="Days of history")
    parser.add_argument("--realtime", action="store_true", help="Only show realtime users")
    args = parser.parse_args()

    token = get_access_token()

    print(f"\n📡 Querying Google Analytics 4 (Property ID: {PROPERTY_ID} - The Vivaak Villa)...")
    rt = get_realtime_report(token)
    rt_rows = rt.get("rows", [])
    total_active = sum(int(r.get("metricValues", [{}])[0].get("value", 0)) for r in rt_rows)
    print(f"\n🟢 Current Realtime Active Users (Last 30 min): {total_active}")
    for r in rt_rows:
        dims = r.get("dimensionValues", [])
        cntry = dims[0].get("value", "")
        city = dims[1].get("value", "")
        users = r.get("metricValues", [{}])[0].get("value", 0)
        print(f"   • Location: {city}, {cntry} -> {users} active user(s)")

    if not args.realtime:
        print(f"\n📈 Historical Daily Performance (Last {args.days} Days):")
        hist = get_daily_report(token, days=args.days)
        h_rows = hist.get("rows", [])
        print(f"\n{'Date':<12} | {'Users':<8} | {'Sessions':<10} | {'Pageviews':<12} | {'Engagement Rate':<15}")
        print("-" * 65)
        for r in h_rows[:args.days]:
            d_raw = r.get("dimensionValues", [{}])[0].get("value", "")
            d_fmt = f"{d_raw[:4]}-{d_raw[4:6]}-{d_raw[6:]}" if len(d_raw) == 8 else d_raw
            m = r.get("metricValues", [])
            users = m[0].get("value", "0") if len(m) > 0 else "0"
            sess = m[1].get("value", "0") if len(m) > 1 else "0"
            pv = m[2].get("value", "0") if len(m) > 2 else "0"
            eng = f"{float(m[3].get('value', 0)) * 100:.1f}%" if len(m) > 3 else "N/A"
            print(f"{d_fmt:<12} | {users:<8} | {sess:<10} | {pv:<12} | {eng:<15}")
    print("")

if __name__ == "__main__":
    main()

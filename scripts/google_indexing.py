#!/usr/bin/env python3
"""
Vivaak & Vaza — Google Indexing API Submitter
Submits updated and new URLs directly to Google for rapid crawling & indexing.
"""

import sys
import json
import urllib.request
import urllib.parse
import os
import argparse

CREDS_FILE = os.path.expanduser("~/.gemini/config/google-credentials.json")

DEFAULT_URLS = [
    "https://vivaak.com/",
    "https://vivaak.com/vivaak-villa/",
    "https://vivaak.com/vaza-villa/",
    "https://vivaak.com/about/",
    "https://vivaak.com/gallery/",
    "https://vivaak.com/blogs/",
    "https://vivaak.com/contact/",
    "https://vivaak.com/faqs/",
    "https://vivaak.com/testimonials/",
    "https://vivaak.com/dharampur-villa/",
    "https://vivaak.com/barog-villa/"
]

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

def submit_url(url, token, action="URL_UPDATED"):
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    payload = {
        "url": url,
        "type": action
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            notify_time = res.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "OK")
            print(f"✅ {url} -> HTTP {resp.status} (Notified: {notify_time})")
            return True
    except Exception as e:
        print(f"⚠️ {url} -> Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Google Indexing API Submitter for Vivaak")
    parser.add_argument("urls", nargs="*", default=DEFAULT_URLS, help="URLs to publish")
    parser.add_argument("--action", default="URL_UPDATED", choices=["URL_UPDATED", "URL_DELETED"], help="Notification type")
    args = parser.parse_args()

    print(f"🔑 Refreshing Google OAuth credentials...")
    token = get_access_token()
    print(f"🚀 Publishing {len(args.urls)} URLs to Google Indexing API...")

    success = 0
    for u in args.urls:
        if submit_url(u, token, action=args.action):
            success += 1

    print(f"\n🎉 Completed: {success}/{len(args.urls)} URLs published to Google Indexing API successfully!\n")

if __name__ == "__main__":
    main()

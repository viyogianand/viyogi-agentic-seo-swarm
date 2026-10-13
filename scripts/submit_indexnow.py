#!/usr/bin/env python3
"""
Vivaak & Vaza — Automated IndexNow & Bing Broadcast Script
Broadcasts URLs immediately to Bing, IndexNow, and search engines.
"""

import sys
import json
import urllib.request
import argparse

INDEXNOW_KEY = "8a4b0421cd964dfcabd3a7b2ef122ce0"
HOST = "vivaak.com"
KEY_LOCATION = f"https://{HOST}/{INDEXNOW_KEY}.txt"

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

def submit_indexnow(urls):
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }

    data = json.dumps(payload).encode("utf-8")
    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow"
    ]

    print(f"🚀 Submitting {len(urls)} URLs to IndexNow protocol ({HOST})...")
    for ep in endpoints:
        try:
            req = urllib.request.Request(
                ep,
                data=data,
                headers={"Content-Type": "application/json; charset=utf-8"}
            )
            with urllib.request.urlopen(req) as resp:
                print(f"✅ {ep}: HTTP {resp.status} (Submission Accepted)")
        except Exception as e:
            print(f"⚠️ {ep}: Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Vivaak IndexNow Submitter")
    parser.add_argument("urls", nargs="*", default=DEFAULT_URLS, help="Optional URLs to submit")
    args = parser.parse_args()

    submit_indexnow(args.urls)

if __name__ == "__main__":
    main()

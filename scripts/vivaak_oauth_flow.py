#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import urllib.request
import json
import os
import subprocess
import sys
import threading

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
PORT = 38888
REDIRECT_URI = f"http://localhost:{PORT}"
CREDENTIALS_PATH = os.path.expanduser("~/.gemini/config/google-credentials.json")
GA4_CREDENTIALS_PATH = os.path.expanduser("~/.gemini/config/ga4-credentials.json")
ADC_CREDENTIALS_PATH = os.path.expanduser("~/.config/gcloud/application_default_credentials.json")
MCP_CONFIG_PATH = os.path.expanduser("~/.gemini/config/mcp_config.json")

SCOPES = [
    "https://www.googleapis.com/auth/webmasters",
    "https://www.googleapis.com/auth/indexing",
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/tagmanager.readonly",
    "https://www.googleapis.com/auth/tagmanager.edit.containers",
    "https://www.googleapis.com/auth/business.manage",
    "https://www.googleapis.com/auth/adwords"
]

params = {
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "response_type": "code",
    "scope": " ".join(SCOPES),
    "access_type": "offline",
    "prompt": "consent"
}

AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)

httpd_server = None

class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)

        if "code" in qs:
            code = qs["code"][0]
            token_url = "https://oauth2.googleapis.com/token"
            data = urllib.parse.urlencode({
                "code": code,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "grant_type": "authorization_code"
            }).encode("utf-8")

            try:
                req = urllib.request.Request(token_url, data=data, method="POST")
                with urllib.request.urlopen(req) as resp:
                    tokens = json.loads(resp.read().decode("utf-8"))
                
                tokens["client_id"] = CLIENT_ID
                tokens["client_secret"] = CLIENT_SECRET
                
                # 1. Save to ~/.gemini/config/google-credentials.json
                os.makedirs(os.path.dirname(CREDENTIALS_PATH), exist_ok=True)
                with open(CREDENTIALS_PATH, "w") as f:
                    json.dump(tokens, f, indent=2)

                # 2. Save authorized user format to ga4-credentials.json
                refresh_token = tokens.get("refresh_token")
                if refresh_token:
                    ga4_dict = {
                        "type": "authorized_user",
                        "client_id": CLIENT_ID,
                        "client_secret": CLIENT_SECRET,
                        "refresh_token": refresh_token
                    }
                    with open(GA4_CREDENTIALS_PATH, "w") as f:
                        json.dump(ga4_dict, f, indent=2)
                    
                    os.makedirs(os.path.dirname(ADC_CREDENTIALS_PATH), exist_ok=True)
                    with open(ADC_CREDENTIALS_PATH, "w") as f:
                        json.dump(ga4_dict, f, indent=2)

                # 3. Update ~/.gemini/config/mcp_config.json
                if os.path.exists(MCP_CONFIG_PATH) and refresh_token:
                    with open(MCP_CONFIG_PATH, "r") as f:
                        mcp_cfg = json.load(f)
                    
                    if "mcpServers" in mcp_cfg:
                        if "gsc-mcp" in mcp_cfg["mcpServers"]:
                            mcp_cfg["mcpServers"]["gsc-mcp"]["env"]["GSC_CLIENT_ID"] = CLIENT_ID
                            mcp_cfg["mcpServers"]["gsc-mcp"]["env"]["GSC_CLIENT_SECRET"] = CLIENT_SECRET
                            mcp_cfg["mcpServers"]["gsc-mcp"]["env"]["GSC_REFRESH_TOKEN"] = refresh_token
                        if "gtm-mcp" in mcp_cfg["mcpServers"]:
                            mcp_cfg["mcpServers"]["gtm-mcp"]["env"]["GOOGLE_CLIENT_ID"] = CLIENT_ID
                            mcp_cfg["mcpServers"]["gtm-mcp"]["env"]["GOOGLE_CLIENT_SECRET"] = CLIENT_SECRET
                            mcp_cfg["mcpServers"]["gtm-mcp"]["env"]["GOOGLE_REFRESH_TOKEN"] = refresh_token
                        if "analytics-mcp" in mcp_cfg["mcpServers"]:
                            mcp_cfg["mcpServers"]["analytics-mcp"]["env"]["GOOGLE_PROJECT_ID"] = "vivaak-5862d"
                        
                        with open(MCP_CONFIG_PATH, "w") as f:
                            json.dump(mcp_cfg, f, indent=2)

                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"""
                    <html>
                    <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; text-align: center; padding: 60px;">
                        <h1 style="color: #10B981; font-size: 32px;">&#10004; Authentication Successful!</h1>
                        <p style="font-size: 18px; color: #374151;">Vivaak Project (vivaak-5862d) Google APIs (Search Console, GA4, GTM, GMB Profile) have been successfully authenticated and synchronized.</p>
                        <p style="color: #6B7280; font-size: 16px;">You can close this tab and return to Antigravity.</p>
                    </body>
                    </html>
                """)
                print("SUCCESS: Tokens successfully saved and configs updated!")
                sys.stdout.flush()

                def shutdown():
                    httpd_server.shutdown()
                threading.Thread(target=shutdown).start()

            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(f"<h1>Error exchanging code</h1><p>{e}</p>".encode("utf-8"))
                print("ERROR exchanging code:", e)
                sys.stdout.flush()

        elif "error" in qs:
            error = qs["error"][0]
            self.send_response(400)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(f"<h1>Authentication Denied</h1><p>{error}</p>".encode("utf-8"))
            print("ERROR from Google:", error)
            sys.stdout.flush()

        elif parsed.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()

        else:
            self.send_response(302)
            self.send_header("Location", AUTH_URL)
            self.end_headers()

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    print("========================================================")
    print("Vivaak Google APIs (vivaak-5862d) OAuth Listener")
    print("========================================================")
    print("Starting listener on:", REDIRECT_URI)
    print("\nIf browser did not open automatically, visit:")
    print(AUTH_URL)
    print("========================================================")
    sys.stdout.flush()

    subprocess.Popen(["open", AUTH_URL])

    socketserver.TCPServer.allow_reuse_address = True
    httpd_server = socketserver.TCPServer(("", PORT), OAuthHandler)
    try:
        httpd_server.serve_forever()
    finally:
        httpd_server.server_close()

# -*- coding: utf-8 -*-
"""
Lightweight Local HTTP Server for Eclipse IDE Web App
Run with: python server.py
Access at: http://localhost:8080
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print(f"=======================================================")
        print(f" Eclipse IDE Java Workspace Web Server")
        print(f" Serving at: {url}")
        print(f" Press Ctrl+C to stop the server.")
        print(f"=======================================================")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run()


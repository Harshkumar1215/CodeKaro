#!/usr/bin/env python3
"""
CODEKARO — Atomic Counter Server
Lightweight Python server for managing database/stats.json with thread-safe atomic writes.
Run this script if hosting CODEKARO on a Python-capable server environment.
"""

import json
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'stats.json')
file_lock = threading.Lock()

def read_stats():
    with file_lock:
        if not os.path.exists(DATABASE_FILE):
            return {"students": 0}
        try:
            with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {"students": 0}

def increment_stats():
    with file_lock:
        data = {"students": 0}
        if os.path.exists(DATABASE_FILE):
            try:
                with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                data = {"students": 0}

        current_count = data.get("students", 0)
        data["students"] = current_count + 1
        data["version"] = data.get("version", 1) + 1

        # Atomic write via temporary file
        temp_file = DATABASE_FILE + '.tmp'
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        os.replace(temp_file, DATABASE_FILE)

        return data

class CounterHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == '/api/counter':
            stats = read_stats()
            response_bytes = json.dumps(stats).encode('utf-8')
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(response_bytes)))
            self.end_headers()
            self.wfile.write(response_bytes)

        elif parsed.path == '/api/counter/up':
            stats = increment_stats()
            response_bytes = json.dumps(stats).encode('utf-8')
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(response_bytes)))
            self.end_headers()
            self.wfile.write(response_bytes)

        else:
            self.send_response(404)
            self._send_cors_headers()
            self.end_headers()

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CounterHandler)
    print(f"CODEKARO Counter Server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

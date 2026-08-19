# app.py - HTTP handler and entrypoint for Vercel / local execution
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        return super().do_GET()

app = handler

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server = HTTPServer(('0.0.0.0', port), handler)
    print(f"Serving at http://localhost:{port}")
    server.serve_forever()

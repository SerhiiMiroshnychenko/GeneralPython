import http.server
import socketserver

port = 8000

with socketserver.TCPServer(('', port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()

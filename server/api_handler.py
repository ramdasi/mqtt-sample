import re
import bson.json_util
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from mongo_handler import fetch_from_mongo

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if re.search('/fetch', self.path):
            parsed_url = urlparse(self.path)
            path = parsed_url.path

            # Extract query parameters
            query_params = parse_qs(parsed_url.query)
            start_time = query_params.get('startTime', [None])[0]
            end_time = query_params.get('endTime', [None])[0]
            docs = fetch_from_mongo(start_time, end_time, "sensorStatuses")

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(bson.json_util.dumps(docs).encode())
        else:
            with open('server/index.html') as f:
                html_content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(html_content.encode())

def start_server():
    global httpd
    httpd = HTTPServer(('localhost', 8000), HTTPRequestHandler)
    print('Starting httpd...\n')
    httpd.serve_forever()
    # print('Stopping httpd...\n')

def stop_server():
    global httpd
    httpd.shutdown()

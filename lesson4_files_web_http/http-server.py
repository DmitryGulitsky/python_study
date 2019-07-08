from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print('In GET request')

        self.send_response(200)
        self.send_header('Content-type', 'text-plain')
        self.end_headers()

        # encode string type data to bytes
        self.wfile.write('Hello World'.encode())

httpd = HTTPServer(('localhost', 8080), MyHandler)

print('Starting...')

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Bye!')
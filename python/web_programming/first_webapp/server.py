import http.server

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message = 'Hello world!' + self.path
        self.wfile.write(message.encode())
        return

def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
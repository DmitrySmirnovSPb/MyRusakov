import http.server

SERVER_ADDRESS = ('localhost', 15253)
http = http.server.HTTPServer(SERVER_ADDRESS,http.server.CGIHTTPRequestHandler)
http.serve_forever()
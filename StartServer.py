import http.server
import socketserver
import threading

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

class ServerThread(threading.Thread):
    def __init__(self, httpd):
        threading.Thread.__init__(self)
        self.httpd = httpd

    def run(self):
        print("Serving at port", PORT)
        self.httpd.serve_forever()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    server_thread = ServerThread(httpd)
    server_thread.start()

    print("Press 'q' to stop the server.")
    while True:
        key = input()
        if key == 'q':
            print("Shutting down the server...")
            httpd.shutdown()
            server_thread.join()
            break
#!/usr/bin/env python
import os
import re
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the routes with regular expressions
ROUTES = [
    (re.compile(r'^/(\d+)/(\d+)/(\d+)$'), '/')
]

class MyHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Default root is the current working directory
        root = os.getcwd()
        
        # Iterate over the routes to find a matching pattern
        for patt, rootDir in ROUTES:
            if patt.match(path):
                # Adjust the path and set the root directory
                path = ''
                root = os.path.join(rootDir, '')
                break
        
        # Construct the new path
        full_path = os.path.join(root, path.lstrip('/'))
        
        # If the path is a directory, serve index.html
        if os.path.isdir(full_path):
            full_path = os.path.join(full_path, 'index.html')
        
        return full_path

if __name__ == '__main__':
    httpd = HTTPServer(('127.0.0.1', 8000), MyHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()

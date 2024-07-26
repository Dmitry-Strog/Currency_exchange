from http.server import BaseHTTPRequestHandler, HTTPServer
from router import routers
import json


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path in routers:
            x = routers[self.path]
            x(self).do_GET()
        else:
            self.send_error(404, "Not Found")


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Сервер стартует на порту {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()

import json
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from router import routers


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/currencies":
            handler = routers.get("/currencies")
            code, response = handler().do_GET()
            self.send(code, response)

        elif self.path.startswith("/currency/"):
            handler = routers.get("/currency/")
            currency_code = self.parse_path(self.path)
            code, response = handler(currency_code).do_GET()
            self.send(code, response)
        elif self.path == "/exchangeRates":
            handler = routers.get("/exchangeRates")
            code, response = handler().do_GET()
            self.send(code, response)
        elif self.path.startswith("/exchangeRate/"):
            handler = routers.get("/exchangeRate/")
            currency_code = self.parse_path(self.path)
            code, response = handler(currency_code).do_GET()
            self.send(code, response)

    def do_POST(self):
        if self.path == "/currencies":
            handler = routers.get("/currencies")
            data = self.parse_post_data()
            code, response = handler().do_POST(dict(data))
            self.send(code, response)
        if self.path == "/exchangeRates":
            handler = routers.get("/exchangeRates")
            data = self.parse_post_data()
            code, response = handler().do_POST(dict(data))
            self.send(code, response)

    def parse_post_data(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        return urllib.parse.parse_qsl(post_data)

    def send(self, code, data):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        response = json.dumps(data, indent=4, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8'))

    @staticmethod
    def parse_path(path: str):
        code = path.lstrip('/').split("/")[-1]
        return code


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Сервер стартует на порту {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from router import routers


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/currency":
            handler = routers.get("/currency")
            response = handler().do_GET()
            self.send(200, response)

        if self.path.startswith("/currency/"):
            handler = routers.get("/currency/")
            currency_code = self.parse_path(self.path)
            response = handler(currency_code).do_GET()
            self.send(200, response)

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

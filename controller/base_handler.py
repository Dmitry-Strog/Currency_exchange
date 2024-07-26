import json
from abc import abstractmethod, ABC
from http.server import BaseHTTPRequestHandler


class BaseHandler(ABC):
    def __init__(self, handler: BaseHTTPRequestHandler):
        self.handler = handler

    @abstractmethod
    def do_GET(self):
        raise NotImplementedError

    @abstractmethod
    def do_POST(self):
        raise NotImplementedError

    def send(self, code, data):

        self.handler.send_response(code)
        self.handler.send_header('Content-Type', 'application/json; charset=utf-8')
        self.handler.end_headers()

        response = json.dumps(data, indent=4, ensure_ascii=False)
        self.handler.wfile.write(response.encode('utf-8'))

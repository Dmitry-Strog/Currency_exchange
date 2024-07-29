import json
from abc import abstractmethod, ABC
from http.server import BaseHTTPRequestHandler


class BaseHandler(ABC):

    @abstractmethod
    def do_GET(self):
        raise NotImplementedError

    @abstractmethod
    def do_POST(self):
        raise NotImplementedError



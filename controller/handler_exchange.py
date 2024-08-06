from controller.base_handler import BaseHandler


class ExchangeHandler(BaseHandler):
    def __init__(self, data):
        self.data = data
        self.dao = None

    def do_GET(self):
        self.data.get("")

    def do_POST(self):
        pass
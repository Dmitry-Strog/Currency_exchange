from controller.base_handler import BaseHandler
from service.exchange_service import ExchangeService


class ExchangeHandler(BaseHandler):
    def __init__(self, data):
        self.data: dict = data
        self.service = ExchangeService(self.data)

    def do_GET(self):
        response_dto = self.service.select_exchange_rate().to_dict()
        return 200, response_dto

    def do_POST(self):
        pass
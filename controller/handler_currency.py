from controller.base_handler import BaseHandler
from dao.dao_currency import DaoCurrency


class CurrencyHandler(BaseHandler):
    def __init__(self, handler):
        super().__init__(handler)
        self.dao = DaoCurrency()

    def do_GET(self):
        currency_dicts = [dto.to_dict() for dto in self.dao.get_currencies_all()]
        self.send(200, currency_dicts)

    def do_POST(self):
        pass

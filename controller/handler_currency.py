from controller.base_handler import BaseHandler
from dao.dao_currency import DaoCurrency


class CurrencyHandler(BaseHandler):
    def __init__(self, code):
        self.code = code
        self._dao = DaoCurrency()

    def do_GET(self):
        currency_dicts = self._dao.get_currency(self.code).to_dict()
        return currency_dicts

    def do_POST(self):
        pass

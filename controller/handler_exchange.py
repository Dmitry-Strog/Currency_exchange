from controller.base_handler import BaseHandler
from dao.exchange_dao import ExchangeRatesDAO
from dto.exchange_dto import ExchangeDTO
from exception import MissingFormField, DatabaseUnavailableException


class ExchangeHandler(BaseHandler):
    def __init__(self):
        self.dao = ExchangeRatesDAO()

    def do_GET(self):
        try:
            currency_dicts = [dto.to_dict() for dto in self.dao.get_exchange_all()]
            return 200, currency_dicts
        except DatabaseUnavailableException as error:
            return 500, {"message": error.message}

    def do_POST(self, data: dict):
        base = data.get('baseCurrencyCode')
        target = data.get('targetCurrencyCode')
        rate = data.get('rate')
        if base is None or target is None or rate is None:
            raise MissingFormField

from controller.base_handler import BaseHandler
from dao.exchange_dao import ExchangeRatesDAO
from dto.exchange_dto import ExchangeDTO
from exception import MissingFormField, DatabaseUnavailableException, CurrencyPairMissingError


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
        try:
            base = data.get('baseCurrencyCode')
            target = data.get('targetCurrencyCode')
            rate = data.get('rate')
            if base is None or target is None or rate is None:
                raise MissingFormField
            base_target_code: tuple = base, target
            dto = ExchangeDTO(None, base, target, rate)
            self.dao.save_exchange_currency(dto)
            currency_dicts = self.dao.get_exchange(base_target_code).to_dict()
            return 201, currency_dicts
        except CurrencyPairMissingError as error:
            return 409, {"message": error.message}
        except MissingFormField as error:
            return 400, {"message": error.message}

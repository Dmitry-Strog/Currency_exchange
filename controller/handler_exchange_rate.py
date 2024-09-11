from controller.base_handler import BaseHandler
from dao.exchange_dao import ExchangeRatesDAO
from dto.exchange_dto import ExchangeDTO
from exception import CurrencyPairMissingError, ExchangeRateNotFoundError, MissingFormField, \
    CurrencyPairMissingException


class ExchangeRateHandler(BaseHandler):
    def __init__(self, code):
        self.code = code
        self._dao = ExchangeRatesDAO()

    def do_GET(self):
        try:
            if len(self.code) != 6:
                raise CurrencyPairMissingError
            base_currency_code = self.code[:3]
            target_currency_code = self.code[3:]
            parse_code = base_currency_code, target_currency_code
            currency_dicts = self._dao.get_exchange(parse_code)
            if not isinstance(currency_dicts, ExchangeDTO):
                raise ExchangeRateNotFoundError
            return 200, currency_dicts.to_dict()

        except CurrencyPairMissingError as error:
            return 400, {"message": error.message}
        except ExchangeRateNotFoundError as error:
            return 404, {"message": error.message}

    def do_POST(self):
        pass

    def do_PATCH(self, rate):
        try:
            base_currency_code = self.code[:3]
            target_currency_code = self.code[3:]
            parse_code = base_currency_code, target_currency_code
            self._dao.update_exchange_rate(parse_code, rate)
            currency_dicts = self._dao.get_exchange(parse_code).to_dict()
            return 200, currency_dicts
        except MissingFormField as error:
            return 400, {"message": error.message}
        except CurrencyPairMissingException as error:
            return 404, {"message": error.message}
from controller.base_handler import BaseHandler
from dao.dao_currency import DaoCurrency
from exception import DatabaseUnavailableException, CurrencyCodeMissingError, CurrencyNotFoundError


class CurrencyHandler(BaseHandler):
    def __init__(self, code):
        self.code = code
        self._dao = DaoCurrency()

    def do_GET(self):
        try:
            if len(self.code) != 3:
                raise CurrencyCodeMissingError
            currency_dicts = self._dao.get_currency(self.code).to_dict()
            return 200, currency_dicts

        except DatabaseUnavailableException as error:
            return 500, {"message": error.message}
        except CurrencyCodeMissingError as error:
            return 400, {"message": error.message}
        except CurrencyNotFoundError as error:
            return 404, {"message": error.message}

    def do_POST(self):
        pass

from controller.base_handler import BaseHandler
from dao.currency_dao import CurrencyDao
from dto.dto_currency import CurrencyDTO
from exception import DatabaseUnavailableException, CurrencyCodeAlreadyExistsError, MissingFormField


class CurrenciesHandler(BaseHandler):
    def __init__(self):
        self.dao = CurrencyDao()

    def do_GET(self):
        try:
            currency_dicts = [dto.to_dict() for dto in self.dao.get_currencies_all()]
            return 200, currency_dicts
        except DatabaseUnavailableException as error:
            return 500, {"message": error.message}

    def do_POST(self, post_data):
        try:
            code = post_data.get('code')
            fullname = post_data.get('fullname')
            sign = post_data.get('sign')
            if code is None or fullname is None or sign is None:
                raise MissingFormField
            dto = CurrencyDTO(None, code, fullname, sign)
            self.dao.save_currency(dto)
            currency_dicts = self.dao.get_currency(code).to_dict()
            return 201, currency_dicts
        except CurrencyCodeAlreadyExistsError as error:
            return 409, {"message": error.message}
        except MissingFormField as error:
            return 400, {"message": error.message}

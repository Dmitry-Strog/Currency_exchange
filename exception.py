class DatabaseUnavailableException(Exception):
    def __init__(self, message="База данных недоступна"):
        self.message = message


class CurrencyCodeMissingError(Exception):
    def __init__(self, message="Код валюты отсутствует в адресе"):
        self.message = message


class MissingFormField(Exception):
    def __init__(self, message="Отсутствует нужное поле формы"):
        self.message = message


class CurrencyNotFoundError(Exception):
    def __init__(self, message="Валюта не найдена"):
        self.message = message


class CurrencyCodeAlreadyExistsError(Exception):
    def __init__(self, message="Валюта с таким кодом уже существует"):
        self.message = message


class ExchangeCodeAlreadyExistsError(Exception):
    def __init__(self, message="Валютная пара с таким кодом уже существует"):
        self.message = message


class CurrencyPairMissingError(Exception):
    def __init__(self, message="Коды валют пары отсутствуют в адресе"):
        self.message = message


class ExchangeRateNotFoundError(Exception):
    def __init__(self, message="Обменный курс для пары не найден"):
        self.message = message


class CurrencyNotFoundException(Exception):
    def __init__(self, message="Одна (или обе) валюта из валютной пары не существует в БД"):
        self.message = message


class CurrencyPairMissingException(Exception):
    def __init__(self, message="Валютная пара отсутствует в базе данных"):
        self.message = message

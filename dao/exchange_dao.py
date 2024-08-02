import sqlite3
from dto.dto_currency import CurrencyDTO
from dto.exchange_dto import ExchangeDTO
from exception import DatabaseUnavailableException, CurrencyNotFoundError, ExchangeCodeAlreadyExistsError, \
    ExchangeRateNotFoundError


class ExchangeRatesDAO:
    def get_exchange_all(self):
        """" Получение всех обменных курсов """
        with sqlite3.connect('exchange.db') as db:
            cur = db.cursor()
            query = cur.execute("SELECT * FROM exchangerates").fetchall()
            dto_list = []
            for elem in query:
                id, base_id, target_id, rate = elem
                base_id = self.get_currency_by_id(base_id).to_dict()
                target_id = self.get_currency_by_id(target_id).to_dict()
                dto_list.append(ExchangeDTO(id, base_id, target_id, rate))
            return dto_list

    def get_exchange(self, data_code: tuple):
        """" Получение конкретного обменного курса """
        try:
            with sqlite3.connect('exchange.db') as db:
                cur = db.cursor()
                query = f"""SELECT e.id, e.base_currency_id, e.target_currency_id, e.rate
                FROM exchangerates e
                JOIN currencies bc ON e.base_currency_id = bc.id
                JOIN currencies tc ON e.target_currency_id = tc.id
                WHERE bc.code = '{data_code[0]}' AND tc.code = '{data_code[1]}'"""
                result = cur.execute(query).fetchall()
                id, base_id, target_id, rate = result[0][0], result[0][1], result[0][2], result[0][3],
                baseCurrency = self.get_currency_by_id(base_id).to_dict()
                targetCurrency = self.get_currency_by_id(target_id).to_dict()
                exchange_dto = ExchangeDTO(id, baseCurrency, targetCurrency, rate)
                return exchange_dto
        except sqlite3.OperationalError:
            raise DatabaseUnavailableException
        except IndexError:
            raise ExchangeRateNotFoundError

    # def save_currency(self, dto: ExchangeDTO):
    #     baseCurrencyCode, targetCurrencyCode, rate = dto.to_dict().values()
    #     base = self.get_currency(baseCurrencyCode).id
    #     target = self.get_currency(targetCurrencyCode).id
    #     try:
    #         with sqlite3.connect('exchange.db') as db:
    #             cur = db.cursor()
    #             query = "INSERT INTO exchangerates (base_currency_id, target_currency_id, rate) VALUES(?,?,?)"
    #             cur.execute(query, (base, target, rate))
    #             db.commit()
    #     except sqlite3.IntegrityError:
    #         raise ExchangeCodeAlreadyExistsError

    def get_currency_by_id(self, id):
        """" Получение валюты из БД """
        try:
            with sqlite3.connect('exchange.db') as db:
                cur = db.cursor()
                query = cur.execute(f"SELECT * FROM currencies WHERE id = '{id}'").fetchall()
                currency_dto = CurrencyDTO(query[0][0], query[0][1], query[0][2], query[0][3])
                return currency_dto
        except sqlite3.OperationalError:
            raise DatabaseUnavailableException
        except IndexError:
            raise CurrencyNotFoundError

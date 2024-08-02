import sqlite3
from dto.dto_currency import CurrencyDTO
from dto.exchange_dto import ExchangeDTO
from exception import DatabaseUnavailableException, CurrencyNotFoundError, ExchangeCodeAlreadyExistsError


class ExchangeRatesDAO:
    def get_exchange_all(self):
        """" Получение всех валютных пар из БД """
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
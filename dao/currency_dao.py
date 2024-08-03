import sqlite3

from dto.dto_currency import CurrencyDTO
from exception import DatabaseUnavailableException, CurrencyNotFoundError, CurrencyCodeAlreadyExistsError


class CurrencyDao:
    def get_currencies_all(self):
        """" Получение всех валют из БД """
        try:
            with sqlite3.connect('exchange.db') as db:
                cur = db.cursor()
                query = cur.execute("SELECT * FROM currencies").fetchall()
                currency_dto_list = [CurrencyDTO(q[0], q[1], q[2], q[3]) for q in query]
                return currency_dto_list
        except sqlite3.OperationalError:
            raise DatabaseUnavailableException

    def get_currency(self, code):
        """" Получение валюты из БД """
        try:
            with sqlite3.connect('exchange.db') as db:
                cur = db.cursor()
                query = cur.execute("SELECT * FROM currencies WHERE code = ?", (code,)).fetchall()
                currency_dto = CurrencyDTO(query[0][0], query[0][1], query[0][2], query[0][3])
                return currency_dto
        except sqlite3.OperationalError:
            raise DatabaseUnavailableException
        except IndexError:
            raise CurrencyNotFoundError

    def save_currency(self, dto):
        id, code, fullname, sign = dto.to_dict().values()
        try:
            with sqlite3.connect('exchange.db') as db:
                cur = db.cursor()
                query = "INSERT INTO currencies (code, fullname, sign) VALUES(?,?,?)"
                cur.execute(query, (code, fullname, sign))
                db.commit()
        except sqlite3.IntegrityError:
            raise CurrencyCodeAlreadyExistsError

if __name__ == '__main__':
    x = CurrencyDao()

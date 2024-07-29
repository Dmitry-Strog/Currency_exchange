import sqlite3

from dto.dto_currency import CurrencyDTO


class DaoCurrency:
    def get_currencies_all(self):
        """" Получение всех валют из БД """
        with sqlite3.connect('exchange.db') as db:
            cur = db.cursor()
            query = cur.execute("SELECT * FROM currencies").fetchall()
            currency_dto_list = [CurrencyDTO(q[0], q[1], q[2], q[3]) for q in query]
            return currency_dto_list

    def get_currency(self, code):
        """" Получение всех валют из БД """
        with sqlite3.connect('exchange.db') as db:
            cur = db.cursor()
            query = cur.execute(f"SELECT * FROM currencies WHERE code = '{code}'").fetchone()
            currency_dto = CurrencyDTO(query[0], query[1], query[2], query[3])
            return currency_dto


if __name__ == '__main__':
    x = DaoCurrency()

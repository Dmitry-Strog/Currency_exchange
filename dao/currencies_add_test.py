import sqlite3


class CurrenciesAddTest:
    def add_currency(self, code, fullname, sign):
        with sqlite3.connect('exchange.db') as db:
            cur = db.cursor()
            query = "INSERT INTO currencies (code, fullname, sign) VALUES(?,?,?)"
            try:
                cur.execute(query, (code, fullname, sign))
                db.commit()
            except sqlite3.IntegrityError:
                print("Такая валюта уже существует")


if __name__ == "__main__":
    date = (
        ("RUB", "Russian Ruble", "₽"),
        ("USD", "United States dollar", "$"),
        ("EUR", "Euro", "€")
    )
    start = CurrenciesAddTest()
    for code, fullname, sign in date:
        start.add_currency(code, fullname, sign)
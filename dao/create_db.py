import sqlite3


class CreateDb:
    def init_db(self):
        self.create_db()
        self.create_currencies_table()
        self.create_exchange_rates_table()

    def create_db(self):
        with sqlite3.connect("exchange.db") as db:
            db.commit()

    def create_currencies_table(self):
        with sqlite3.connect("exchange.db") as db:
            cur = db.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS currencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code VARCHAR(50) NOT NULL UNIQUE,
            fullname VARCHAR(50) NOT NULL UNIQUE,
            sign VARCHAR(50) NOT NULL UNIQUE
            )""")
            db.commit()

    def create_exchange_rates_table(self):
        with sqlite3.connect("exchange.db") as db:
            cur = db.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS exchangerates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            base_currency_id INTEGER NOT NULL UNIQUE,
            target_currency_id INTEGER NOT NULL UNIQUE,
            rate DECIMAL(6) NOT NULL,
            FOREIGN KEY (base_currency_id) REFERENCES currencies (id),
            FOREIGN KEY (target_currency_id) REFERENCES currencies (id),
            CONSTRAINT unique_ID UNIQUE (base_currency_id, target_currency_id)
            )""")
            db.commit()


if __name__ == '__main__':
    CreateDb().init_db()

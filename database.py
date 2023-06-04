import sqlite3
import os


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS stock_data
                          (symbol TEXT, date TEXT, close REAL, shares INTEGER)''')

    def insert_stock_data(self, stock_data):
        cursor = self.conn.cursor()
        for stock in stock_data:
            symbol = stock.symbol
            date = stock.date
            close_price = float(stock.close) if isinstance(stock.close, (float, int)) else None
            shares = stock.shares

            cursor.execute('INSERT INTO stock_data VALUES (?, ?, ?, ?)', (symbol, date, close_price, shares))

        self.conn.commit()

    def retrieve_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT symbol, date, close, shares FROM stock_data')
        return cursor.fetchall()

    def remove_db_file(self):
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

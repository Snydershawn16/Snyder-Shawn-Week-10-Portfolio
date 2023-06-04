from database import Database
from json_handler import read_json
from plotter import plot_stock_data
from stock import Stock
import json


def process_data(file_path):
    try:
        # Load JSON data from file
        stock_data = read_json(file_path)

        # Delete the existing database file if it exists
        db.remove_db_file()

        # Connect to the database
        db.connect()

        # Create a new table for existing stock data
        db.create_table()

        # Convert stock_data to Stock objects
        stocks = []
        for stock in stock_data:
            symbol = stock['Symbol']
            date = stock['Date']
            close_price = stock['Close']
            shares = stock.get('Shares', 0)  # Use default value of 0 if 'Shares' key is missing
            stocks.append(Stock(symbol, date, close_price, shares))

        # Insert existing stock data into the database
        db.insert_stock_data(stocks)

        # Disconnect from the database
        db.disconnect()

        # Reconnect to retrieve data for plotting
        db.connect()

        # Retrieve data from the database
        data = db.retrieve_data()

        # Disconnect from the database
        db.disconnect()

        # Plot the stock data
        plot_stock_data(data)

    except FileNotFoundError:
        print("File Not Found: The selected file does not exist.")
    except json.JSONDecodeError:
        print("Invalid JSON: The selected file is not a valid JSON file.")


if __name__ == "__main__":
    file_path = 'AllStocks.json'
    db = Database('portfolio.db')
    process_data(file_path)

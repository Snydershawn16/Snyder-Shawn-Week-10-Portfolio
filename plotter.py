import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt


def plot_stock_data(data):
    symbols = list(set([row[0] for row in data]))
    dates = sorted(list(set([row[1] for row in data])))

    for symbol in symbols:
        symbol_dates = [row[1] for row in data if row[0] == symbol]
        symbol_values = [row[2] for row in data if row[0] == symbol]

        # Create a DataFrame with the stock data
        df = pd.DataFrame({'Date': symbol_dates, 'Close': symbol_values})
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Add missing columns with dummy values
        df['Open'] = df['Close']
        df['High'] = df['Close']
        df['Low'] = df['Close']
        df['Volume'] = 0

        # Plot the stock data using mplfinance
        mpf.plot(df, type='candle', style='yahoo', title=f'{symbol} Stock', ylabel='Price')

    plt.show()

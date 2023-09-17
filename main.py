# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(round(price , 2))

    return closingList

stocks = ['MSFT', 'OSK', 'NVDA', 'KR', 'INTC']

for stock in stocks:
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing)+1))

#This creates the graph
    plt.plot(days, stockClosing)

#gets min and max for the y axis
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    days = range(1, len(stockClosing) + 1)

#This plots the graph for the stock
    plt.plot(days, stockClosing)

#This makes labels for the graph
    plt.xlabel('Days')
    plt.ylabel('closing price')
    plt.title('Closing Price for' + stock)
    plt.axis([1, 10 ,low_price -3, high_price + 3])
    plt.show()
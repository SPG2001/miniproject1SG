# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path

# This grabs the stock information from yfinance and grabs the closing price information for the last 10 days

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(round(price , 2))

    return closingList

def printGraph(stock):

    # Runs through each stock in the list and makes a graph.
        stockClosing = np.array(getClosing(stock))
        days = list(range(1, len(stockClosing) + 1))

        # This creates the graph
        plt.plot(days, stockClosing)

        # gets min and max for the y axis
        prices = getClosing(stock)
        prices.sort()
        low_price = prices[0]
        high_price = prices[-1]

        # Sets the min and max of the x axis, as well as the y axis.
        plt.axis([1, 10, low_price, high_price])


        days = range(1, len(stockClosing) + 1)

        # This plots the graph for the stock
        plt.plot(days, stockClosing)

        # This makes labels for the graph
        plt.xlabel('Days')
        plt.ylabel('closing price')
        # Creates the charts file and saves the charts to it.
        savefile = "charts/" + stock + ".png"
        plt.savefig(savefile)


        #Finally shows the charts.
        plt.show()

def stockInput():

    stocks = []

    print('Please enter five stocks to graph')
    for i in range(1, 6):

        while True:
            print('Enter stock ticker number ' + str(i))
            ticker = input("> ")
            try:
                stock = yf.Ticker(ticker)
                stock.info
                stocks.append(ticker)
                print('Input accepted.')
                break
            except:
                print("That is not a valid stock. Please enter a valid stock.")

    return stocks

    # Creates the charts file and saves the charts to it.

try:
    Path("charts").mkdir()
except FileExistsError:
    pass


for stock in stockInput():
    getClosing(stock)
    printGraph(stock)
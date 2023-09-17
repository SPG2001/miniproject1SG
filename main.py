# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path

#This grabs the stock information from yfinance and grabs the closing price information for the last 10 days

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(round(price , 2))

    return closingList

#Creates the charts file and saves the charts to it.
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

#List of stocks I would like to see the prices of.
stocks = ['MSFT', 'OSK', 'NVDA', 'KR', 'INTC']


#Runs through each stock in the dictionary and makes a graph.
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
    plt.title('Closing Price for ' + stock)
    plt.axis([1, 10, low_price -3, high_price + 3])

    savefile = "charts/" + stock + '.png'
    plt.savefig(savefile)

    #Displays the charts.
    plt.show()
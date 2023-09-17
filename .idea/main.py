# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 1

import numpy as np
import matplotlib as plt
import yfinance as yf
import pprint

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(round(price , 2))

    return closingList

stocks = ['MSFT', 'OSK', 'NVDA', 'KR', 'INTC']

stocks = np.array(stocks)

msft = getClosing('MSFT')

print(msft)

# get all stock info
#pprint.pprint(msft.info)

# get historical market data
#hist = msft.history(period="10d")

#for price in hist['Close']:
    #print(price)
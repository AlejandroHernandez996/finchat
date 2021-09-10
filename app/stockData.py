import yfinance as yf

class StockData(object):
    def __init__(self, t):
        self.ticker = yf.Ticker(t)
        self.history = self.ticker.history(period="1d",interval="1h")
    def getHistory(self):
        return self.history
    def getCurrentPrice(self):
        return self.ticker.info['regularMarketPrice']

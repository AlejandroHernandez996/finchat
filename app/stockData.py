import yfinance as yf

class StockData(object):
    def __init__(self, t):
        self.history = yf.Ticker(t).history(period="2y",interval="1wk")
    def getHistory(self):
        return self.history
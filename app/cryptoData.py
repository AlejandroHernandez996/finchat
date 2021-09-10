import cryptocompare

class CryptoData(object):
    def __init__(self, t):
        self.ticker = t
    def getCurrentPrice(self):
        return cryptocompare.get_price(self.ticker, currency='USD', full=True)['DISPLAY'][self.ticker]['USD']['PRICE'].split()[1]

import yfinance as yf

class Stock():
    def __init__(self,name,period="1d",interval="5m"):
        self.name = name
        self.symbol = name+".NS"
        self.period = period
        self.interval = interval
        self.ticker = yf.Ticker(self.symbol)
        self.df = self.ticker.history(period=period,interval=interval)
        self.current = self.df.iloc[-1]
    
    def refresh(self):
        self.ticker = yf.Ticker(self.symbol)
        self.df = self.ticker.history(period=self.period, interval=self.interval)
        self.current = self.df.iloc[-1]

    def __str__(self):
        return("{name} Close: {close} at {time}".format(name = self.name , close = self.current["Close"] , time = self.df.index[-1]))

if __name__ == '__main__':
    ticker = 'AAPL'
    ticker = yf.Ticker(ticker)  # initializing the object
    df = ticker.history(period="1d", interval="5m")
    ticker = Stock('TECHM')
    print(ticker)
    print(ticker.df)
import yfinance as yf
import matplotlib.pyplot as plt

#pick a stock
ticker = "AAPL"


#download stock data of 6 months
data = yf.download(ticker, period="10mo")

#calculate daily returns
data["Return"] = data["Close"].pct_change()

#calculate MA
data["MA20"] = data["Close"].rolling(window=20).mean() #this is the 20 Moving average
data["MA50"] = data["Close"].rolling(window=50).mean() #this is the 50 Moving Average 

#plot the closing prices
plt.figure(figsize=(12,6))
plt.plot(data.index, data["Close"], label="Close price")
plt.plot(data.index, data["MA20"], label="20-day MA")
plt.plot(data.index, data["MA50"], label="50-day MA")
plt.title(f"{ticker} with moving average")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()

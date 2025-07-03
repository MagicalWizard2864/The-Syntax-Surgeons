#old code from quant.py
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

print(df.head())

# Plot the closing price
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='AAPL Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.title('AAPL Closing Price in 2024')
plt.legend()
plt.grid(True)
plt.show()

#upated code from quant.py file
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
df2 = yf.download("NFLX", start="2024-01-01", end="2024-12-31")


print(df.head())
print(df2.head())


# Plot the closing price
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='AAPL Close Price')
plt.plot(df2.index, df2['Close'], label='NFLX Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.title('AAPL Closing Price in 2024')
plt.legend()
plt.grid(True)
plt.show()

# Plot the closing price in two subplots
fig, ax = plt.subplots(2, 1, figsize=(10, 5))
ax[0].plot(df.index, df['Close'], label='AAPL Close Price')
ax[0].set_title('AAPL Closing Price in 2024')
ax[0].set_ylabel('Close Price (USD)')
ax[0].legend()
ax[0].grid(True)

ax[1].plot(df2.index, df2['Close'], label='NFLX Close Price')
ax[1].set_title('NFLX Closing Price in 2024')
ax[1].set_ylabel('Close Price (USD)')
ax[1].legend()
ax[1].grid(True)
plt.show()

#open,high,low,close,volume
plt.plot(df.index, df['Open'], label='AAPL Open Price')
plt.plot(df.index, df['High'], label='AAPL High Price')
plt.plot(df.index, df['Low'], label='AAPL Low Price')
plt.plot(df.index, df['Close'], label='AAPL Close Price')
plt.plot(df.index, df['Volume'], label='AAPL Volume')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the moving average
df['MA50'] = df['Close'].rolling(window=50).mean()
df2['MA50'] = df2['Close'].rolling(window=50).mean()

# Plot the moving average
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['MA50'], label='AAPL MA50')
plt.plot(df2.index, df2['MA50'], label='NFLX MA50')
plt.legend()
plt.grid(True)

#daily returns
df['Daily Return'] = df['Close'].pct_change()
df2['Daily Return'] = df2['Close'].pct_change()

# Plot the daily returns
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Daily Return'], label='AAPL Daily Return')
plt.plot(df2.index, df2['Daily Return'], label='NFLX Daily Return')
plt.legend()
plt.grid(True)

#histogram of returns
plt.figure(figsize=(10, 5))
plt.hist(df['Daily Return'], bins=50, alpha=0.5, label='AAPL Daily Return')
plt.hist(df2['Daily Return'], bins=50, alpha=0.5, label='NFLX Daily Return')
plt.legend()
plt.grid(True)
plt.show()

#correlation between AAPL and NFLX
print(df.corr(df2))

#plot the correlation
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='AAPL Close Price')
plt.plot(df2.index, df2['Close'], label='NFLX Close Price')
plt.legend()
plt.grid(True)
plt.show()

#candlestick chart
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='AAPL Close Price')
plt.plot(df2.index, df2['Close'], label='NFLX Close Price')
plt.legend()
plt.grid(True)
plt.show()

#volume analysis
plt.plot(df.index, df['Volume'], label='AAPL Volume')
plt.plot(df2.index, df2['Volume'], label='NFLX Volume')
plt.legend()
plt.grid(True)
plt.show()

#correlation between AAPL and NFLX
print(df.corr(df2))

#volatility
df['Volatility'] = df['Close'].rolling(window=20).std()
df2['Volatility'] = df2['Close'].rolling(window=20).std()

# Plot the volatility
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Volatility'], label='AAPL Volatility')
plt.plot(df2.index, df2['Volatility'], label='NFLX Volatility')
plt.legend()
plt.grid(True)

#in this code every visulization works and no errors fount in this 

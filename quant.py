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

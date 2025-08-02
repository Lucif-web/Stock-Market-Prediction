import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta


df = pd.read_csv('GIME_dataset.csv', parse_dates=['Date'])


df.sort_values('Date', inplace=True)
df.set_index('Date', inplace=True)

print(df.head())

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='GBIME Close Price', color='blue')
plt.title('GBIME Stock Price (2021–Now)')
plt.xlabel('Date')
plt.ylabel('Price (NPR)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


df['RSI'] = ta.rsi(df['Close'], length=14)
macd = ta.macd(df['Close'])
df = pd.concat([df, macd], axis=1)

# Print last few to verify
print(df[['Close', 'RSI', 'MACD_12_26_9', 'MACDs_12_26_9']].tail())

# Plot closing price + RSI
plt.figure(figsize=(14, 8))

# Plot 1: Closing Price
plt.subplot(3, 1, 1)
plt.plot(df['Close'], label='Close Price', color='blue')
plt.title('GBIME Stock Price with RSI and MACD')
plt.grid(True)
plt.legend()

# Plot 2: RSI
plt.subplot(3, 1, 2)
plt.plot(df['RSI'], label='RSI', color='orange')
plt.axhline(70, color='red', linestyle='--', linewidth=1)
plt.axhline(30, color='green', linestyle='--', linewidth=1)
plt.grid(True)
plt.legend()

# Plot 3: MACD
plt.subplot(3, 1, 3)
plt.plot(df['MACD_12_26_9'], label='MACD', color='purple')
plt.plot(df['MACDs_12_26_9'], label='Signal', color='grey')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

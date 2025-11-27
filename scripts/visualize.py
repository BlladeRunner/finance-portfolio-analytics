import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DB_PATH = "db/portfolio.db"

# ---------- Load KPI Table ----------
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM kpis", conn)
conn.close()

print(df.head())

# ---------- 1. Bar Chart: Annual Return ----------
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="ticker", y="annual_ret", palette="viridis")
plt.title("Annual Returns by Ticker (%)")
plt.ylabel("Annual Return (%)")
plt.xlabel("Ticker")
plt.tight_layout()
plt.savefig("outputs/annual_return.png")
plt.show()

# ---------- 2. Risk/Return Scatter ----------
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df, 
    x="vol_annual", 
    y="annual_ret", 
    hue="ticker", 
    s=200
)
plt.title("Risk vs Return (Annual Volatility vs Annual Return)")
plt.xlabel("Annual Volatility")
plt.ylabel("Annual Return (%)")
plt.axhline(0, color="gray", linestyle="--", linewidth=1)
plt.tight_layout()
plt.savefig("outputs/risk_return.png")
plt.show()

# ---------- 3. Daily Price Trends ----------
conn = sqlite3.connect(DB_PATH)
prices = pd.read_sql_query("""
SELECT ticker, date, adj_close
FROM prices
ORDER BY date ASC;
""", conn)
conn.close()

plt.figure(figsize=(14, 7))
for ticker in prices["ticker"].unique():
    subset = prices[prices["ticker"] == ticker]
    plt.plot(subset["date"], subset["adj_close"], label=ticker)

plt.title("Daily Price Trend")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/price_trends.png")
plt.show()
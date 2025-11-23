# 📊 Finance Portfolio Analytics

A professional data analytics project for evaluating **stock performance**, **portfolio returns**, **volatility**, and **risk metrics** using **Python**, **Pandas**, **SQLite**, and **SQL analytics**.

This project is part of a Data Analyst portfolio and demonstrates:

* Data ingestion from financial APIs
* Portfolio construction & asset weighting
* SQL-based analytical calculations
* Python-based financial KPIs
* Clean folder structure & reproducible workflow

---

## 🚀 Project Goals
1. Build a reusable analytics pipeline for financial data.
2. Compute portfolio-level metrics:

   * Daily returns
   * Cumulative returns
   * Volatility
   * Sharpe Ratio
   * Max Drawdown
3. Store data in a relational SQL database.
4. Prepare the dataset for a future Dashboard (Power BI or Streamlit).
5. Demonstrate real‑world analytical workflow.

---

## 📁 Project Structure
```
finance-portfolio-analytics/
│
├── data/
│   └── raw/                # Financial raw CSV files
│
├── db/
│   └── portfolio.db        # SQLite database
│
├── scripts/
│   ├── fetch_data.py       # Download historical market data
│   ├── compute_metrics.py   # Portfolio KPIs (Sharpe, volatility, returns)
│   └── load_to_sql.py       # Insert cleaned data into SQLite
│
├── sql/
│   ├── sanity.sql          # Basic validation checks
│   └── metrics.sql         # SQL queries for KPIs
│
├── outputs/                # Charts and analytics (will be generated)
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack
* **Python 3.10+**
* **Pandas** — data processing
* **yfinance** — financial data API
* **SQLite** — lightweight database
* **SQL** — analytical queries
* **Matplotlib / Seaborn** — charts (coming soon)

---

## 🔧 Setup Instructions
### 1. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Fetch Market Data

```bash
python scripts/fetch_data.py
```

### 4. Load Data Into SQLite

```bash
python scripts/load_to_sql.py
```

### 5. Run SQL Checks

You can run sanity checks using:

```sql
SELECT COUNT(*) FROM prices;
SELECT * FROM portfolio_daily LIMIT 5;
```

---

## 📈 KPIs Included
* **Daily Returns**
* **Cumulative Portfolio Growth**
* **Volatility (Std Dev)**
* **Sharpe Ratio (Risk‑Adjusted Return)**
* **Max Drawdown**
* **Correlation Matrix**

---

## 📊 Planned Visualizations (Coming Soon)
✔ Portfolio value over time
✔ Rolling volatility
✔ Asset allocation chart
✔ Moving Sharpe ratio
✔ Correlation heatmap

These charts will be generated in the `/outputs` folder.

---

## 📦 Next Steps
* Build SQL-powered KPI dashboard
* Add interactive Streamlit UI
* Export Power BI version

---

If you like this project, feel free to ⭐ star the repository!

[🔙 **Back to Portfolio**](https://github.com/BlladeRunner)

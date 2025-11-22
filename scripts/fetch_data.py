import sqlite3
from pathlib import Path
from datetime import date

import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DB_PATH = ROOT / "db" / "portfolio.db"

DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

TICKERS = [
    "AAPL",  # Apple
    "MSFT",  # Microsoft
    "GOOGL", # Alphabet
    "AMZN",  # Amazon
    "TSLA",  # Tesla
    "META",  # Meta
    "NVDA",  # Nvidia
    "VOO",   # Vanguard S&P 500 ETF
    "QQQ",   # Nasdaq 100 ETF
    "GLD",   # Gold ETF
    "BTC-USD"  # Bitcoin
]

START_DATE = "2018-01-01"
INTERVAL = "1d"


def fetch_prices():
    print(f"[INFO] Downloading {len(TICKERS)} tickers from Yahoo Finance...")
    df = yf.download(
        tickers=TICKERS,
        start=START_DATE,
        end=None,          
        interval=INTERVAL,
        auto_adjust=False,
        group_by="ticker",
        progress=False,
        threads=True,
    )

    if isinstance(df.columns, pd.MultiIndex):
        frames = []
        for ticker in TICKERS:
            if ticker not in df.columns.levels[0]:
                print(f"[WARN] Ticker {ticker} not found in downloaded data, skipping")
                continue

            tdf = df[ticker].reset_index()  # Date + OHLCV
            tdf["ticker"] = ticker
            tdf = tdf.rename(
                columns={
                    "Date": "date",
                    "Open": "open",
                    "High": "high",
                    "Low": "low",
                    "Close": "close",
                    "Adj Close": "adj_close",
                    "Volume": "volume",
                }
            )
            frames.append(tdf)

        if not frames:
            raise RuntimeError("No data downloaded for any ticker.")
        all_df = pd.concat(frames, ignore_index=True)
    else:
        df = df.reset_index()
        df["ticker"] = TICKERS[0]
        all_df = df.rename(
            columns={
                "Date": "date",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Adj Close": "adj_close",
                "Volume": "volume",
            }
        )

    all_df["date"] = pd.to_datetime(all_df["date"]).dt.date.astype(str)
    for col in ["open", "high", "low", "close", "adj_close"]:
        all_df[col] = pd.to_numeric(all_df[col], errors="coerce")
    all_df["volume"] = pd.to_numeric(all_df["volume"], errors="coerce").astype("Int64")

    all_df = all_df.sort_values(["ticker", "date"]).reset_index(drop=True)

    csv_path = DATA_DIR / "prices.csv"
    all_df.to_csv(csv_path, index=False)
    print(f"[OK] Saved CSV: {csv_path} ({len(all_df):,} rows)")

    return all_df


def load_to_sqlite(df: pd.DataFrame):
    print(f"[INFO] Writing data to SQLite: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS prices;

    CREATE TABLE prices (
        ticker      TEXT NOT NULL,
        date        TEXT NOT NULL,   -- 'YYYY-MM-DD'
        open        REAL,
        high        REAL,
        low         REAL,
        close       REAL,
        adj_close   REAL,
        volume      INTEGER,
        PRIMARY KEY (ticker, date)
    );
    """)

    df.to_sql("prices", conn, if_exists="append", index=False)
    conn.commit()

    # sanity-check
    rows = cur.execute("SELECT COUNT(*) FROM prices;").fetchone()[0]
    min_d, max_d = cur.execute(
        "SELECT MIN(date), MAX(date) FROM prices;"
    ).fetchone()

    conn.close()
    print(f"[OK] Written {rows:,} rows into prices.")
    print(f"[INFO] Date range: {min_d} → {max_d}")


def main():
    print(f"[START] Fetching portfolio data @ {date.today().isoformat()}")
    df = fetch_prices()
    load_to_sqlite(df)
    print("[DONE] Portfolio data ready in db/portfolio.db and data/prices.csv")


if __name__ == "__main__":
    main()

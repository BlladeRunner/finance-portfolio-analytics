from pathlib import Path
import sqlite3
import pandas as pd
import math

DB_PATH = Path("db/portfolio.db")
SQL_PATH = Path("sql/kpis.sql")
OUT_CSV = Path("outputs/kpis.csv")

print("[INFO] Reading SQL…")
query = SQL_PATH.read_text(encoding="utf-8")

print("[INFO] Running KPI query against SQLite…")
with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query(query, conn)

print("[INFO] Computing volatility and annual return in pandas…")
# the standard deviation of the daily return
df["vol_daily"] = df["var_daily"].pow(0.5)
# annual volatility (252 trading days)
df["vol_annual"] = df["vol_daily"] * math.sqrt(252)
# annual return at daily_ret as the average daily return
df["annual_ret"] = (1 + df["avg_daily_ret"]) ** 252 - 1

df = df[["ticker", "avg_daily_ret", "vol_daily", "vol_annual", "annual_ret", "var_daily", "n"]]

print("[INFO] Writing table 'kpis' into SQLite…")
with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("kpis", conn, if_exists="replace", index=False)

print(f"[INFO] Saving CSV → {OUT_CSV}")
OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_CSV, index=False)

print("[INFO] Done. KPIs are stored in table 'kpis' and outputs/kpis.csv")

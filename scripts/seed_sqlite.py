import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("db/portfolio.db")
PRICES_PATH = Path("data/prices.csv")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

with open("sql/schema.sql", "r", encoding="utf-8") as f:
    cur.executescript(f.read())

df = pd.read_csv(PRICES_PATH)

df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

print("CSV columns:", df.columns.tolist())

df.to_sql("prices", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ Database seeded successfully.")

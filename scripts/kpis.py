import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "db" / "portfolio.db"
SQL_PATH = ROOT / "sql" / "kpis.sql"
OUT_PATH = ROOT / "outputs" / "kpis.csv"

print("[INFO] Reading SQL…")
query = Path(SQL_PATH).read_text()

print("[INFO] Connecting to database…")
conn = sqlite3.connect(DB_PATH)

print("[INFO] Executing query…")
df = pd.read_sql_query(query, conn)

print("[INFO] Saving CSV…")
OUT_PATH.parent.mkdir(exist_ok=True)
df.to_csv(OUT_PATH, index=False)

print("[DONE] KPI exported →", OUT_PATH)

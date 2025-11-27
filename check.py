import sqlite3
import json
from pathlib import Path

DB_PATH = Path("db/portfolio.db")

print(f"[INFO] Using DB: {DB_PATH.resolve()}")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# List tables and views
objects = cur.execute(
    "SELECT name, type FROM sqlite_master WHERE type IN ('table','view') ORDER BY type, name;"
).fetchall()

print("\n[INFO] Objects in sqlite_master:")
print(json.dumps(objects, indent=2))

# Try reading from kpis
print("\n[INFO] Preview from kpis (if exists):")
try:
    rows = cur.execute("SELECT * FROM kpis LIMIT 5;").fetchall()
    print(json.dumps(rows, indent=2))
except Exception as e:
    print(f"  -> Cannot read kpis: {e}")

conn.close()

print("\n[INFO] Done.")

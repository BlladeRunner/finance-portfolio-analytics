DROP TABLE IF EXISTS prices;

CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker      TEXT    NOT NULL,
    date        TEXT    NOT NULL,
    open        REAL,
    high        REAL,
    low         REAL,
    close       REAL,
    adj_close   REAL,
    volume      INTEGER
);


DROP TABLE IF EXISTS portfolio_holdings;
CREATE TABLE portfolio_holdings (
    ticker TEXT PRIMARY KEY,
    quantity REAL NOT NULL,
    avg_cost REAL NOT NULL
);

DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    date TEXT NOT NULL,
    type TEXT CHECK(type IN ('BUY','SELL')),
    quantity REAL NOT NULL,
    price REAL NOT NULL
);

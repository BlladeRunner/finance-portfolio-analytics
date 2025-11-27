DROP VIEW IF EXISTS v_returns;

CREATE VIEW v_returns AS
SELECT
    ticker,
    date,
    adj_close,
    LAG(adj_close) OVER (PARTITION BY ticker ORDER BY date) AS prev_close,
    (adj_close * 1.0 / LAG(adj_close) OVER (PARTITION BY ticker ORDER BY date) - 1.0) AS daily_ret
FROM prices;

DROP VIEW IF EXISTS v_monthly_perf;

CREATE VIEW v_monthly_perf AS
SELECT
    ticker,
    substr(date, 1, 7) AS month,
    (MAX(adj_close) * 1.0 / MIN(adj_close) - 1.0) AS monthly_ret
FROM prices
GROUP BY ticker, substr(date, 1, 7);


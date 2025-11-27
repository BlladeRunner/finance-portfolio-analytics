-- Basic sanity checks for prices table

-- 1) Rows count
SELECT COUNT(*) AS rows_in_prices
FROM prices;

-- 2) Date range
SELECT MIN(date) AS min_date,
       MAX(date) AS max_date
FROM prices;

-- 3) Tickers list
SELECT DISTINCT ticker
FROM prices
ORDER BY ticker;

-- 4) Any NULL prices?
SELECT ticker,
       COUNT(*) AS rows,
       SUM(CASE WHEN adj_close IS NULL THEN 1 ELSE 0 END) AS null_adj_close
FROM prices
GROUP BY ticker
ORDER BY null_adj_close DESC;

SELECT COUNT(*) AS rows_in_prices FROM prices;

SELECT ticker,
       MIN(date) AS min_date,
       MAX(date) AS max_date,
       COUNT(*)  AS rows_per_ticker
FROM prices
GROUP BY ticker;

SELECT * FROM v_returns LIMIT 10;
SELECT * FROM v_monthly_perf LIMIT 10;
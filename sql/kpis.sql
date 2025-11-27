-- sql/kpis.sql
-- Basic KPIs for tickers based on daily returns

WITH r AS (
    SELECT
        ticker,
        date,
        daily_ret
    FROM v_returns
    WHERE daily_ret IS NOT NULL
),
stats AS (
    SELECT
        ticker,
        AVG(daily_ret) AS avg_daily_ret,
        -- variance: E[x^2] - (E[x])^2
        AVG(daily_ret * daily_ret) - AVG(daily_ret) * AVG(daily_ret) AS var_daily,
        COUNT(*) AS n
    FROM r
    GROUP BY ticker
)
SELECT
    ticker,
    avg_daily_ret,
    var_daily,
    n
FROM stats;

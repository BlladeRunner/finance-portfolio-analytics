-- sql/kpis.sql

WITH r AS (
    SELECT
        ticker,
        date,
        daily_ret,
        daily_ret * daily_ret AS ret_sq
    FROM v_returns
    WHERE daily_ret IS NOT NULL
),
stats AS (
    SELECT
        ticker,
        AVG(daily_ret)              AS avg_daily_ret,
        AVG(ret_sq)                 AS avg_ret_sq,
        COUNT(*)                    AS n
    FROM r
    GROUP BY ticker
)
SELECT
    ticker,
    avg_daily_ret,
    -- variance = E[x^2] - (E[x])^2
    sqrt( avg_ret_sq - avg_daily_ret * avg_daily_ret )          AS vol_daily,
    sqrt(252) * sqrt( avg_ret_sq - avg_daily_ret * avg_daily_ret ) AS vol_annual,
    ( (1 + avg_daily_ret) * 252 - 1 )                           AS annual_ret
FROM stats
ORDER BY annual_ret DESC;

SELECT date, daily_sales,
SUM(daily_sales) OVER(
    ORDER BY date
    ROWS BETWEEN 1 PRECEDING and 1 FOLLOWING
    ) AS moving_total,
AVG(daily_sales) OVER(
    ORDER BY date
    ROWS BETWEEN 1 PRECEDING and 1 FOLLOWING)
    AS moving_average,
from wf_sales
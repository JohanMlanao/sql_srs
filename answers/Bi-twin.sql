SELECT date, daily_sales,
SUM(daily_sales) OVER(
    ORDER BY date
    ROWS BETWEEN 2 PRECEDING and CURRENT ROW
    ) AS moving_total_three_last_rows,
SUM(daily_sales) OVER(
    ORDER BY date
    ) AS running_total,
from wf_sales
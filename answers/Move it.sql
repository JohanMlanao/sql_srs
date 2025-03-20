SELECT *,
SUM(daily_sales) OVER(ORDER BY date) as running_total,
COUNT(daily_sales) OVER(ORDER BY date) as running_count,
AVG(daily_sales) OVER(ORDER BY date) as running_mean,
from wf_sales
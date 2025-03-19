WITH TOTAL_SALES_PER_CLIENT AS (
    SELECT SUM(amount) AS total_sales
    FROM gb_sales
    GROUP BY client
),

MEAN_TOTAL_SALES AS (
    SELECT MEAN(total_sales)
    FROM TOTAL_SALES_PER_CLIENT
)

SELECT client,
SUM(amount) as total_sales
FROM gb_sales
GROUP BY CLIENT
HAVING total_sales >
(SELECT * FROM MEAN_TOTAL_SALES)
ORDER BY client
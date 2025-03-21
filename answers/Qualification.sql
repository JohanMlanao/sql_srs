SELECT *,
DENSE_RANK() OVER(
    PARTITION BY sex
    ORDER BY wage DESC
    ) AS index
FROM wages
QUALIFY index = 2
ORDER BY name
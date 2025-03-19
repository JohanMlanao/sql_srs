SELECT client, AVG(amount)
FROM gb_sales
GROUP BY client
ORDER BY client
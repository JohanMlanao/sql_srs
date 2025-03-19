SELECT client, AVG(amount)
FROM gb_sales
GROUP BY client
HAVING AVG(amount) > (SELECT AVG(amount) FROM gb_sales)
ORDER BY client
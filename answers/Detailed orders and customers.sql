SELECT *
FROM orders
INNER JOIN order_details
USING(order_id)
INNER JOIN customers
USING (customer_id)
SELECT
c.customer_id,
customer_name,
o.order_id,
od.product_id,
od.quantity
FROM customers as c
LEFT JOIN orders as o
USING (customer_id)
LEFT JOIN order_details as od
ON o.order_id = od.order_id
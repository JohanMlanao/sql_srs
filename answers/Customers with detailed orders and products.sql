SELECT
c.customer_id,
customer_name,
o.order_id,
od.product_id,
od.quantity,
p.product_name,
p.product_price
FROM customers as c
LEFT JOIN orders as o
USING (customer_id)
LEFT JOIN order_details as od
ON o.order_id = od.order_id
LEFT JOIN products as p
USING (product_id)
SELECT
o.order_id,
o.customer_id,
od.product_id,
od.quantity
FROM orders as o
LEFT JOIN order_details as od
ON o.order_id = od.order_id
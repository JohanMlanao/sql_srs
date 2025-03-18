SELECT
f.customer_id as customer_id,
f.order_id as first_order,
f.date as date_first_order,
s.order_id as second_order,
s.date as date_next_order
FROM self_sales as f
LEFT JOIN self_sales as s
USING (customer_id)
WHERE f.order_id != s.order_id AND s.date - f.date == 1
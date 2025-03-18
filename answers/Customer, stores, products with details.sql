SELECT *
FROM full_customers
LEFT JOIN full_stores
USING (customer_id)
LEFT JOIN full_store_products
USING (store_id)
FULL OUTER JOIN full_products
USING (product_id)


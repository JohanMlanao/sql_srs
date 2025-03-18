SELECT *
FROM sales_custom
LEFT JOIN product_category_custom
USING (product_id)
LEFT JOIN universe_category_custom
USING (category_id)
WHERE universe_name IS NULL
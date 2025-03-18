SELECT *
FROM sales
LEFT JOIN product_category
USING (product_id)
LEFT JOIN universe_category
USING (category_id)
WHERE universe_name IS NULL
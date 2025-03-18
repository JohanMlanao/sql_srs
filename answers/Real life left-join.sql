SELECT *
FROM sales
LEFT JOIN product_category
USING (product_id)
LEFT JOIN universe_category
USING (category_id)
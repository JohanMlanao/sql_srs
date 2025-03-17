SELECT *
FROM sales
INNER JOIN product_category
USING (product_id)
INNER JOIN universe_category
USING (category_id)

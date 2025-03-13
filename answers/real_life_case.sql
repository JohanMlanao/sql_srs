SELECT *
FROM stores
CROSS JOIN markets
CROSS JOIN months
CROSS JOIN days
CROSS JOIN quarters
WHERE day_of_week = 7
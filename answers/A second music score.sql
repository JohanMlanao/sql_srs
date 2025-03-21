WITH max_salaries_per_dpt AS (
    SELECT *,
    MAX(wage) OVER(PARTITION BY department) as max_dpt_wage,
    wage >= max_dpt_wage as is_max
    FROM wages
    )

SELECT name, wage, department, max_dpt_wage,
MAX(wage) OVER(PARTITION BY department) as second_max_dpt_wage
FROM max_salaries_per_dpt
WHERE is_max = FALSE
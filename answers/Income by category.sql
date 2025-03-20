WITH salary_range AS (
SELECT
    name,
    department,
    wage,
    CASE
    WHEN wage <= 50000 THEN 'Low'
    WHEN wage < 90000 THEN 'Medium'
    ELSE 'High'
    END AS salary_range,
  FROM
    wages
)

SELECT
  department,
  salary_range,
  AVG(wage) AS average_salary,
  COUNT(name) as nb_employees
FROM
  salary_range
GROUP BY
  department,
  salary_range
ORDER BY department, salary_range
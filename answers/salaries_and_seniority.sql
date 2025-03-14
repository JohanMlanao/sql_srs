SELECT *
FROM salaries
INNER JOIN seniority
ON salaries.employee_id = seniority.employee_id

-- OR

--SELECT *
-- FROM salaries
-- CROSS JOIN seniority
-- WHERE salaries.employee_id = seniority.employee_id
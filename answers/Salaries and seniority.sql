SELECT salary, employee_id, seniority
FROM salaries
INNER JOIN seniority
ON salaries.employee_id = seniority.employee_id

-- OR

--SELECT salary, employee, seniority
-- FROM salaries
-- CROSS JOIN seniority
-- WHERE salaries.employee_id = seniority.employee_id
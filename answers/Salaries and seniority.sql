SELECT salary, sal.employee_id, seniority
FROM salaries as sal
INNER JOIN seniority as sen
ON salaries.employee_id = seniority.employee_id

-- OR

--SELECT salary, employee, seniority
-- FROM salaries
-- CROSS JOIN seniority
-- WHERE salaries.employee_id = seniority.employee_id
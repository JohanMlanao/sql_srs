SELECT salary, sal.employee_id, seniority
FROM salaries as sal
INNER JOIN seniority as sen
ON sal.employee_id = sen.employee_id

-- OR

--SELECT salary, sal.employee, seniority
-- FROM salaries as sal
-- CROSS JOIN seniority as sen
-- WHERE sal.employee_id = sen.employee_id
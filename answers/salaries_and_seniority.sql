SELECT *
FROM salaries
INNER JOIN seniority
ON salaries.employee_id = seniority.employee_id
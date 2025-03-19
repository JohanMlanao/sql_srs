SELECT
contract_type AS typology,
SUM(reimbursement_amount)
FROM health_care
GROUP BY contract_type

UNION

SELECT procedure_type AS typology,
SUM(reimbursement_amount)
FROM health_care
GROUP BY procedure_type
ORDER BY typology

-- OR
--SELECT
--COALESCE(contract_type, procedure_type) as typology,
--SUM(reimbursement_amount)
--FROM health_care
--GROUP BY GROUPING SETS
--(contract_type, procedure_type)
--ORDER BY typology

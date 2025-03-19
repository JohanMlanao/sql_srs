SELECT contract_type, procedure_type, SUM(reimbursement_amount)
FROM health_care
GROUP BY CUBE
(contract_type, procedure_type)
ORDER BY contract_type, procedure_type
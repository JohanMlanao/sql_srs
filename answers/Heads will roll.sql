SELECT contract_type, procedure_type, age_group, sex, years,
SUM(reimbursement_amount)
FROM health_care
GROUP BY ROLLUP
( contract_type, procedure_type, age_group, sex, years )
ORDER BY contract_type, procedure_type, age_group, sex, years
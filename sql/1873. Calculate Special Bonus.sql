SELECT
    employee_id,
CASE WHEN
    MOD(employee_id, 2)=1 AND name not like 'M%' THEN salary ELSE 0 END AS bonus
FROM
    Employees
ORDER BY
    employee_id
;

-- like 'M%': start with M
-- CASE WHEN ... AND ... THEN ... ELSE ... END
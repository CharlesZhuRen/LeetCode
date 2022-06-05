SELECT
    e.employee_id
FROM
    employees AS e LEFT OUTER JOIN salaries AS s ON e.employee_id = s.employee_id
WHERE
    s.salary IS NULL
UNION
SELECT
    s.employee_id
FROM
    employees AS e RIGHT OUTER JOIN salaries AS s ON e.employee_id = s.employee_id
WHERE
    e.name IS NULL
ORDER BY
    employee_id;


-- 1. look for those doesn't have salary
-- 2. look for those doesn't have name
-- 3. union 1 and 2. union itself can remove duplicates
SELECT 
    MAX(salary) AS SecondHighestSalary 
FROM
    Employee
WHERE 
    salary < (SELECT MAX(salary) FROM Employee)
;

-- the second highest == max(salary < the 1st highest)
-- However, when it comes to 3rd highest, 4th highest, etc, it will be troublesome to select...

-- then there is a better way:
SELECT
    (SELECT DISTINCT
            salary
        FROM
            Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;

-- use ORDER BY and LIMIT 1 OFFSET 1 to select the second highest one
-- use double SELECT to return null if the second highest one doesn't exist
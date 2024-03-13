-- # Write your MySQL query statement below
-- SELECT a.name as Employee
-- FROM employee a
-- WHERE a.salary > (SELECT b.salary FROM employee b WHERE b.id = a.managerid)

SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary
;

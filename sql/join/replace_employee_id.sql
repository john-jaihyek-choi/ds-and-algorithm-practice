-- Leetcode #1378
-- Write your PostgreSQL query statement below
-- Input:
    -- Employees:
        -- id (pk): int
        -- name: varchar
    -- EmployeeUNI:
        -- id (composite pk): int
        -- unique_id (composite pk): int
-- Output:
    -- Output:
        -- unique_id: int
        -- name: varchar
-- Goal:
    -- return the list of unique_id and name of users
        -- if unique id for the user doesn't exist, replace with null
-- Idea:
    -- left join employee and employeeuni
        -- left join will populate as employee table as many rows

SELECT unique_id, name
FROM employees
LEFT JOIN employeeuni ON employees.id = employeeuni.id;

SELECT unique_id, name
FROM employeeuni
RIGHT JOIN employees ON employees.id = employeeuni.id;


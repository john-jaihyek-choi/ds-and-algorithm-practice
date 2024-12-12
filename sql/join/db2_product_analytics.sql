-- DataLemur: https://datalemur.com/questions/sql-ibm-db2-product-analytics
-- Input:
  -- queries:
    -- employee_id: int
    -- query_id: int
    -- query_starttime: datetime
    -- execution_time: int
  -- employees:
    -- employee_id: int
    -- full_name: string
    -- gender: string
-- Goal:
  -- given table queries and employees, return the number of unique queries and the number of employees that made unique_queries many times queries
-- Output:
  -- Output:
    -- unique_queries: int
    -- employee_count: int
-- Idea:
  -- 1. find the employee query counts
    -- with employees table, LEFT JOIN on queries
      -- filter during JOIN for July - September
  -- 2. count the distinct employees in the employee query table
    -- count should be integer which represents the count of query_id
      -- count should also include employees that made 0 queries

WITH employees_q_count AS (
  SELECT
    e.employee_id,
    COALESCE(COUNT(DISTINCT q.query_id)) AS q_count
  FROM employees e
  LEFT JOIN queries q
    ON q.employee_id = e.employee_id
      AND q.query_starttime >= '07/01/2023'
      AND q.query_starttime < '10/01/2023'
  GROUP BY e.employee_id
)

SELECT
  q_count AS unique_queries,
  COUNT(employee_id) AS employee_count
FROM employees_q_count
GROUP BY q_count
ORDER BY q_count;



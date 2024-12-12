-- Leetcode #1581
-- Write your PostgreSQL query statement below
-- Input:
    -- Visits:
        -- visit_id: int
        -- customer_id: int
    -- Transactions:
        -- transaction_id: int
        -- visit_id: int
        -- amount: int
-- Output:
    -- Output:
        -- customer_id: int
        -- count_no_trans
-- Goal:
    -- given tables, visits and transactions, find all ids of users who visted without making transactions and the count of the type of visits for each id
-- Idea:
    -- join the visits and transactions table with visit_id in each table
    -- filter for customer_id that's in the visits table but not in the transaction table

SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM visits v
LEFT JOIN transactions t ON t.visit_id = v.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;



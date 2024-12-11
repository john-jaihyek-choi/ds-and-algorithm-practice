-- Leetcode #584
-- Write your PostgreSQL query statement below
-- Input:
    -- Customer:
        -- id (pk): int
        -- name: varchar
        -- referee_id: int
-- Output:
    -- Output:
        -- name: varchar
-- Goal:
    -- Given a customer table, return names of all customers NOT REFERRED BY the customer with id = 2

-- Idea:
    -- use a where clause on customer table for referee_id <> 2 OR referee_id IS NULL

SELECT name
FROM Customer
WHERE referee_id <> 2
    OR referee_id IS NULL;

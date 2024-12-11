-- Leetcode #1757
-- Write your PostgreSQL query statement below
-- Input:
    -- product_id (pk): int
    -- low_fats: enum
        -- Y == low fat
        -- N == NOT low fat
    -- recyclable: enum
        -- Y == recyclable
        -- N == NOT recyclable
-- Output:
    -- product_id: int
-- Goal:
    -- given products table, return the product ids that are both low fat and recyclable

-- Idea:
    -- filter on products where low_fats == Y and recyclable == N

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
    AND recyclable = 'Y'

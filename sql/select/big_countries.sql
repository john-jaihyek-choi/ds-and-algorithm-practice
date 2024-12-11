-- Leetcode #595
-- Write your PostgreSQL query statement below
-- Input:
    -- World:
        -- name (pk): varchar
        -- continent: varchar
        -- area: int
        -- population: int
        -- gdp: bigint
-- Output:
    -- Output:
        -- name: varchar
        -- population: int
        -- area: int
-- Goal:
    -- given table, World, return big countries:
        -- count == big if...
            -- area >= 3,000,000
            -- OR
            -- population >= 25,000,000
    -- return in any order
-- Idea:
    -- use WHERE clause to filter for name, population, area where population >= 25,000,000 OR area >= 3,000,000

SELECT name, population, area
FROM world
WHERE area >= 3000000
    OR population >= 25000000
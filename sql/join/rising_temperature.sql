-- Leetcode #197
-- Write your PostgreSQL query statement below
-- Input:
    -- Weather:
        -- id: int
        -- recordDate: date
        -- temperature: int
-- Goal:
    -- return the list of weather ids where the temp is higher compared to its previous date (yesterday)
-- Output:
    -- Output:
        -- id: int
-- Ideas:
    -- self join the weather table on dateddiff w1.recordDate and w2.recordDate = 1
    -- return the id where w1.temperature > w2.temperature

-- Solution 1:
-- Using LAG and LEAD
WITH weather_chart AS (
    SELECT 
        *,
        LEAD(recordDate) OVER (ORDER BY recordDate DESC) AS yesterday,
        LEAD(temperature) OVER (ORDER BY recordDate DESC) AS yesterday_temp
    FROM weather
)

SELECT id
FROM weather_chart
WHERE temperature > yesterday_temp


-- Solution 2:
-- Using self-join
WITH weather_comparison AS (
    SELECT 
        w1.id,
        w1.recordDate AS w1_date, w1.temperature AS w1_temp,
        w2.recordDate AS w2_date, w2.temperature AS w2_temp
    FROM weather w1
    JOIN weather w2 ON w1.recordDate = w2.recordDate + INTERVAL '1 day'
)

SELECT id
FROM weather_comparison
WHERE w1_temp > w2_temp;
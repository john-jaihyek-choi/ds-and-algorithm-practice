-- DataLemur: https://datalemur.com/questions/click-through-rate
-- Note:
  -- keywords:
    -- events table on Facebook app analytics
    -- calculate the click through rate
    -- app in 2022
    -- round results to 2 decimal places
  -- definitions:
    -- % of CTR = 100.0 * No of clicks / No of impressions
-- Input:
  -- events:
    -- app_id: integer
    -- event_type: string
    -- timestamp: datetime
-- Output:
  -- output:
    -- app_id: integer
    -- ctr: decimal
-- Goal:
  -- given events table, return % CTR for app in 2022

-- Ideas:
  -- 1. get grouped result of distinct app with distinct event type for 2022 (click_and_impression_counts)
    -- count all clicks
    -- count all impressions
    -- group by app_id, event_type
    -- filter by year 2022
  -- 2. get click count and impression counts from click_and_impression_counts and calculate CTR


-- Initial Try
WITH click_and_impression_counts AS (
  SELECT
    e.app_id,
    COUNT(CASE WHEN e.event_type = 'click' THEN 1 END) as click_count,
    COUNT(CASE WHEN e.event_type = 'impression' THEN 1 END) as impression_count
  FROM events e
  WHERE EXTRACT(YEAR FROM e.timestamp) = '2022'
  GROUP BY app_id
)

SELECT
  app_id,
  ROUND((100.0 * click_count / impression_count), 2) as ctr
FROM click_and_impression_counts


-- 2nd Try
SELECT
  e.app_id,
  ROUND(
    100.0 *
    COUNT(CASE WHEN e.event_type = 'click' THEN 1 END) /
    COUNT(CASE WHEN e.event_type = 'impression' THEN 1 END),
    2) AS ctr 
FROM events e
WHERE EXTRACT(YEAR FROM e.timestamp) = '2022'
GROUP BY e.app_id
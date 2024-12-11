-- Leetcode #1148
-- Write your PostgreSQL query statement below
-- Input:
    -- Views:
        -- article_id: int
        -- author_id: int
        -- viewer_id: int
        -- view_date: date
            -- YYYY-MM-DD
    -- Note:
        -- author_id == viewer_id indicates same person
-- Output:
    -- Output:
        -- id: int
-- Goal:
    -- given table, Views with no primary key, return list of ids of authors that viewed at least 1 of their own articles
        -- sort by id in asc
-- Idea:
    -- If viewer_id == author_id, author viewed their own article
        -- use where clause where author_id = viewr_id

SELECT DISTINCT author_id AS id
FROM views
WHERE author_id = viewer_id
ORDER BY id ASC
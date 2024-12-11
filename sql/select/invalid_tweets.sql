-- Leetcode #1683
-- Write your PostgreSQL query statement below
-- Input:
    -- Tweets:
        -- tweet_id (PK): int
        -- content: varchar
    -- Note:
        -- american keyboard, no other special characters
        -- table contains all tweets in a social media app
-- Output:
    -- Output:
        -- tweet_id (pk): int
-- Goal:
    -- given table, Tweets, return return distinct tweet_ids of the invalid tweets
        -- tweet is invalid if...
            -- number of char used in the content of the twee is greater than 15
-- Idea:
    -- filter for tweet_id on tweets table where CHAR_LENGTH(content) > 15

SELECT tweet_id
FROM tweets
WHERE CHAR_LENGTH(content) > 15;
-- DataLemur: https://datalemur.com/questions/sql-highest-grossing
-- Input:
  -- product_spend
    -- category: str
    -- product: str
    -- user_id: int
    -- spend: decimal
    -- transaction_date: timestamp
-- Output:
  -- output:
    -- category: str
    -- product: str
    -- total_spend: decimal
-- Note:
  -- table containing data about:
    -- customers and their spending on products in various categories
  -- need a query to identify
    -- top 2 highest-grossing products in EACH CATEGORY
    -- for year 2022
  -- output should include category, product, and total spend
-- Idea:
  -- keywords:
    -- top 2 highest grossing (sum of spending for category)
    -- in each category (for all unique category)
    -- year 2022 (01/01/2022 <= transaction_date < 01/01/2023)
  -- steps:
    -- 1. find total spend per category and product (spending_per_category_and_product)
      -- group by category and product
      -- filter on year 2022
      -- order by category asc, spend desc for readability
    -- 2. rank the spending_per_category_and_product by spending (ranked_spendings)
    -- 3. take the rank 1 and 2 spending from ranked_spendings result

WITH spending_per_category_and_product AS (
  SELECT
    category,
    product,
    SUM(spend) AS spend
  FROM product_spend
  WHERE EXTRACT(YEAR FROM transaction_date) = '2022'
  GROUP BY category, product
  ORDER BY category, spend DESC
),

ranked_spendings AS (
  SELECT
    category,
    product,
    spend,
    RANK() OVER (PARTITION BY category ORDER BY spend DESC) AS rank
  FROM spending_per_category_and_product
)

SELECT category, product, spend AS total_spend
FROM ranked_spendings
WHERE rank <= 2
ORDER BY category, spend DESC;
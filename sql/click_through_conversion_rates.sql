-- DataLemur Q6: https://datalemur.com/blog/ibm-sql-interview-questions#Question-6
-- Input:
    -- product_views:
        -- view_id: int
        -- user_id: int
        -- view_date: datetime
        -- product_id: int
    -- product_cart:
        -- cart_id: int
        -- user_id: int
        -- add_to_cart_date: datetime
        -- product_id: int
    -- product_purchases:
        -- purchase_id: int
        -- user_id: int
        -- purchase_date: datetime
        -- product_id: int
-- Output:
    -- product_id: int
    -- cart_adds: int
    -- purchases: int
    -- conversion_rate: decimal
-- Notes:
    -- keywords:
        -- analyze the click-through conversion rates for digital products
            -- number of times a product is viewed
            -- number of times a product is added to the cart
            -- number of times a product is purchased
    -- definition:
        -- CTCR:
            -- (purchases / product views) * 100
-- Ideas:
    -- Needs...
        -- number of time product is viewed
        -- number of times product is added to cart
        -- number of time product is purchased
    -- Find...
        -- view to cart ratio
        -- cart to purchase ratio
        -- view to purchase ratio
    -- Steps:
        -- 1. find number of views for a distinct product
        -- 2. find number of time a product is added to cart
        -- 3. find number of purchases for product
        -- 4. calculate:
            -- view to cart ratio
            -- cart to purchase ratio
            -- view to purchase ratio

WITH views_by_product AS (
    SELECT
        product_id,
        COUNT(DISTINCT user_id) AS views
    FROM product_views
    GROUP BY product_id
),

cart_by_product AS (
    SELECT
        product_id,
        COUNT(DISTINCT cart_id) AS added_to_cart
    FROM product_cart
    GROUP BY product_id
),

purchase_by_product AS (
    SELECT
        product_id,
        COUNT(DISTINCT user_id) AS purchases
    FROM product_purchases
    GROUP BY product_id
)

SELECT
    vbp.product_id,
    COALESCE(vbp.views, 0) AS views,
    COALESCE(cbp.added_to_cart, 0) AS cart_adds,
    COALESCE(pbp.purchases, 0) AS purchases,
    COALESCE(
        ROUND(
            pbp.purchases / vbp.views,
            2
        ),
        0
    ) AS conversion_rate
FROM views_by_product vbp
LEFT JOIN cart_by_product cbp ON cbp.product_id = vbp.product_id
LEFT JOIN purchase_by_product pbp ON pbp.product_id = vbp.product_id;

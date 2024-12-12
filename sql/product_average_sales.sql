-- DataLemur Q8: https://datalemur.com/blog/ibm-sql-interview-questions#Question-8
-- Note:
    -- keywords:
        -- analyze sales data from ecommerce platform
        -- find average sales quantity for each product on monthly basis
    -- definition:
        -- avg_sales_qt = avg(monthly qt)
-- Idea:
    -- 1. get avg of quantity group by month and by product_id

SELECT
    strftime('%m', sale_date) AS "month",
    product_id AS product,
    ROUND(AVG(quantity),2) AS avg_quantity
FROM sales
GROUP BY "month", product

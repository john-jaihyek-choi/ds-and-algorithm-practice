-- DataLemur Q8: https://datalemur.com/blog/ibm-sql-interview-questions#Question-9
-- Note:
    -- keywords:
        -- total amount spent by each customers
        -- total number of orders placed by each customer
-- Ideas:
    -- 1. get aggregate of total spending grouped by distinct customer_id
    -- 2. get aggregate of total orders (order_id) grouped by distict customer_id

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.order_total) AS total_spending,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
LEFT JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
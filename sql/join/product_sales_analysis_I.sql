-- Leetcode #1068
-- Write your PostgreSQL query statement below
-- Input:
    -- Sales:
        -- sale_id (pk): int
        -- product_id (fk): int
        -- year (pk): int
        -- quantity: int
        -- price: int
    -- Product:
        -- product_id (pk): int
        -- product_name: varchar
-- Output:
    -- Output:
        -- product_name: varchar
        -- year: int
        -- price: int
-- Goal:
    -- given tables, sales and product, return the name, year, and price of the product for each sale_id in sales
-- Idea:
    -- join sales with product table and return its product_name, year, and price

SELECT product_name, year, price
FROM sales
JOIN product ON product.product_id = sales.product_id



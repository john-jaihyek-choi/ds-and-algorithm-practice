-- DataLemur Q6: https://datalemur.com/blog/ibm-sql-interview-questions#Question-6
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    sale_date DATETIME NOT NULL,
    quantity INTEGER NOT NULL
);

INSERT INTO sales (sale_id, product_id, customer_id, sale_date, quantity)
VALUES
(1, 1001, 123, '2022-03-01', 10),
(2, 1002, 265, '2022-03-04', 5),
(3, 1001, 478, '2022-03-15', 7),
(4, 1003, 192, '2022-04-01', 3),
(5, 1002, 123, '2022-04-05', 8);

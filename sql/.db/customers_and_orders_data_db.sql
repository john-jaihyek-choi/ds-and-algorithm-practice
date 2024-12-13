-- DataLemur Q6: https://datalemur.com/blog/ibm-sql-interview-questions#Question-6
PRAGMA foreign_keys = ON;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_total DECIMAL NOT NULL,
    order_date DATETIME NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

INSERT INTO customers (customer_id, first_name, last_name)
VALUES
(101, 'John', 'Doe'),
(102, 'Jane', 'Smith'),
(103, 'Michael', 'Johnson'),
(104, 'Emma', 'Wilson'),
(105, 'Oliver', 'Taylor');

INSERT INTO orders (order_id, customer_id, order_total, order_date)
VALUES
(1001, 101, 200.00, '2022-06-25'),
(1002, 101, 300.00, '2022-07-10'),
(1003, 102, 150.00, '2022-06-14'),
(1004, 103, 250.00, '2022-07-05'),
(1005, 104, 350.00, '2022-06-30'),
(1006, 105, 300.00, '2022-07-20'),
(1007, 101, 100.00, '2022-08-01');
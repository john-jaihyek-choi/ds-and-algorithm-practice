-- DataLemur Q6: https://datalemur.com/blog/ibm-sql-interview-questions#Question-6
CREATE TABLE product_views (
    view_id INTEGER PRIMARY KEY,         -- Unique identifier for each view
    user_id INTEGER NOT NULL,            -- ID of the user who viewed the product
    view_date DATETIME NOT NULL,         -- Date and time the product was viewed
    product_id INTEGER NOT NULL          -- ID of the product that was viewed
);

CREATE TABLE product_cart (
    cart_id INTEGER PRIMARY KEY,         -- Unique identifier for each cart entry
    user_id INTEGER NOT NULL,            -- ID of the user who added the product to the cart
    add_to_cart_date DATETIME NOT NULL,  -- Date and time the product was added to the cart
    product_id INTEGER NOT NULL          -- ID of the product that was added to the cart
);

CREATE TABLE product_purchases (
    purchase_id INTEGER PRIMARY KEY,     -- Unique identifier for each purchase
    user_id INTEGER NOT NULL,            -- ID of the user who made the purchase
    purchase_date DATETIME NOT NULL,     -- Date and time the product was purchased
    product_id INTEGER NOT NULL          -- ID of the product that was purchased
);

INSERT INTO product_views (view_id, user_id, view_date, product_id)
VALUES
(211, 4895, '2022-06-10 00:00:00', 1325),
(364, 2375, '2022-06-08 00:00:00', 3452),
(897, 4403, '2022-06-14 00:00:00', 1325),
(999, 3318, '2022-07-04 00:00:00', 9648);

INSERT INTO product_cart (cart_id, user_id, add_to_cart_date, product_id)
VALUES
(113, 4895, '2022-06-11 00:00:00', 1325),
(570, 2375, '2022-06-09 00:00:00', 3452),
(953, 4403, '2022-06-15 00:00:00', 1325);

INSERT INTO product_purchases (purchase_id, user_id, purchase_date, product_id)
VALUES
(118, 4895, '2022-06-12 00:00:00', 1325),
(596, 2375, '2022-06-10 00:00:00', 3452);
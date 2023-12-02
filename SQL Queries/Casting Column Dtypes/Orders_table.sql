ALTER TABLE orders_table 
ALTER COLUMN date_uuid TYPE UUID
USING (CAST(date_uuid AS UUID));

ALTER TABLE orders_table 
ALTER COLUMN user_uuid TYPE UUID
USING (CAST(user_uuid AS UUID));

-- (SELECT MAX(length(card_number)) FROM orders_table)
ALTER TABLE orders_table 
ALTER COLUMN card_number TYPE VARCHAR(19);


-- (SELECT MAX(length(store_code)) FROM orders_table)
ALTER TABLE orders_table 
ALTER COLUMN store_code TYPE VARCHAR(12);

-- (SELECT MAX(length(product_code)) FROM orders_table)
ALTER TABLE orders_table 
ALTER COLUMN product_code TYPE VARCHAR(11);


ALTER TABLE orders_table
ALTER COLUMN product_quantity TYPE SMALLINT;

SELECT * FROM orders_table;


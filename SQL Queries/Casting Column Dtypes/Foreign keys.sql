--  PRIMARY KEY ASSINGMENT 

-- dim_card_details - card_number

-- dim_date_times - date_uuid

-- dim_products - product_code

-- dim_store_details - store_code

-- dim_users - user_uuid


-- ALTER TABLE dim_card_details ADD PRIMARY KEY (card_number);

-- ALTER TABLE dim_date_times ADD PRIMARY KEY (date_uuid);

-- ALTER TABLE dim_products ADD PRIMARY KEY (product_code);

-- ALTER TABLE dim_store_details ADD PRIMARY KEY (store_code);

-- ALTER TABLE dim_users ADD PRIMARY KEY (user_uuid);




-- FOREIGN KEY ASSIGNMENT
-- Foreign keys are either a column or a group of columns in a 
-- relational database table that provide a link between other tables

-- ALTER TABLE orders_table
-- ADD CONSTRAINT card_number_id
-- FOREIGN KEY (card_number)
-- REFERENCES dim_card_details (card_number);


-- ALTER TABLE orders_table
-- ADD CONSTRAINT date_uuid_id
-- FOREIGN KEY (date_uuid)
-- REFERENCES dim_date_times (date_uuid);


-- ALTER TABLE orders_table
-- ADD CONSTRAINT product_code_id
-- FOREIGN KEY (product_code)
-- REFERENCES dim_products (product_code);


-- ALTER TABLE orders_table
-- ADD CONSTRAINT store_code_id
-- FOREIGN KEY (store_code)
-- REFERENCES dim_store_details (store_code);


-- ALTER TABLE orders_table
-- ADD CONSTRAINT user_uuid_id
-- FOREIGN KEY (user_uuid)
-- REFERENCES dim_users (user_uuid);




SELECT * FROM orders_table;



ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255)
USING SUBSTRING(first_name FROM 1 FOR 255);

ALTER TABLE dim_users
ALTER COLUMN last_name TYPE VARCHAR(255)
USING SUBSTRING(last_name FROM 1 FOR 255);

ALTER TABLE dim_users
ALTER COLUMN date_of_birth TYPE DATE;


-- SELECT MAX(length(country_code)) FROM dim_users
ALTER TABLE dim_users
ALTER COLUMN country_code TYPE VARCHAR(2);

ALTER TABLE dim_users
ALTER COLUMN user_uuid TYPE UUID
USING CAST(user_uuid AS UUID);


ALTER TABLE dim_users
ALTER COLUMN join_date TYPE DATE;

SELECT * FROM dim_users
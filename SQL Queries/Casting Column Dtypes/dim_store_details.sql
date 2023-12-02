-- Replaces null values with N/A
-- UPDATE dim_store_details
-- SET address = COALESCE(address, 'N/A')
-- SET longitude = COALESCE(longitude, 'N/A')
-- SET locality = COALESCE(locality, 'N/A')
-- SET latitude = COALESCE(latitude, 'N/A')



ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT
USING NULLIF(longitude, 'N/A')::FLOAT;

ALTER TABLE dim_store_details
ALTER COLUMN latitude TYPE FLOAT
USING NULLIF(latitude, 'N/A')::FLOAT;

ALTER TABLE dim_store_details
ALTER COLUMN locality TYPE VARCHAR(255);

-- SELECT MAX(length(store_code)) FROM dim_store_details
ALTER TABLE dim_store_details
ALTER COLUMN store_code TYPE VARCHAR(12);

ALTER TABLE dim_store_details
ALTER COLUMN staff_numbers TYPE SMALLINT
USING staff_numbers::smallint;

ALTER TABLE dim_store_details
ALTER COLUMN opening_date TYPE DATE;

-- SELECT MAX(length(country_code)) FROM dim_store_details
ALTER TABLE dim_store_details
ALTER COLUMN country_code TYPE VARCHAR(2);

ALTER TABLE dim_store_details
ALTER COLUMN continent TYPE VARCHAR(255);

ALTER TABLE dim_store_details
ALTER COLUMN store_type TYPE VARCHAR(255), 
ALTER COLUMN store_type DROP NOT NULL;


SELECT * FROM dim_store_details



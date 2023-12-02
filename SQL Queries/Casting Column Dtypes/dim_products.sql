-- Add a new column weight_class and populate it based on the weight range
-- ALTER TABLE dim_products
-- ADD COLUMN weight_class VARCHAR(50);

-- UPDATE dim_products
-- SET weight_class = 
--   CASE 
--     WHEN weight < 2 THEN 'Light'
--     WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
--     WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
--     WHEN weight >= 140 THEN 'Truck_Required'
--     ELSE NULL -- Handle any other cases
--   END;


-- ALTER TABLE dim_products
-- 	RENAME removed TO availablity;

ALTER TABLE dim_products
	ALTER COLUMN availablity TYPE BOOLEAN
	USING 
		(CASE
		   WHEN availablity = 'Still_avaliable' THEN True 
		   WHEN availablity = 'Removed' THEN false
		 END);


ALTER TABLE dim_products
	ALTER COLUMN product_price TYPE FLOAT;

ALTER TABLE dim_products
	ALTER COLUMN weight TYPE FLOAT;

-- SELECT MAX(length("EAN")) FROM dim_products
ALTER TABLE dim_products
	ALTER COLUMN "EAN" TYPE VARCHAR(17);

-- SELECT MAX(length(product_code)) FROM dim_products
ALTER TABLE dim_products
	ALTER COLUMN product_code TYPE VARCHAR(11);

ALTER TABLE dim_products
	ALTER COLUMN date_added TYPE DATE;

	


ALTER TABLE dim_products
	ALTER COLUMN uuid TYPE UUID
	USING (CAST(uuid AS UUID));
	
-- SELECT length(MAX(weight_class)) FROM dim_products
ALTER TABLE dim_products
	ALTER COLUMN weight_class TYPE VARCHAR(14);
	
	
	
SELECT * FROM dim_products




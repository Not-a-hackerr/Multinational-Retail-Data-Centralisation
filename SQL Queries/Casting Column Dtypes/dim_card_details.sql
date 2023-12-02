-- SELECT MAX(CHAR_LENGTH(card_number)) AS max_length
-- FROM dim_card_details;
ALTER TABLE dim_card_details
	ALTER COLUMN card_number TYPE VARCHAR(19);
	
-- SELECT length(MAX(expiry_date)) FROM dim_card_details;
ALTER TABLE dim_card_details
	ALTER COLUMN expiry_date TYPE VARCHAR(5);

ALTER TABLE dim_card_details
	ALTER COLUMN date_payment_confirmed TYPE DATE;


SELECT * FROM dim_card_details
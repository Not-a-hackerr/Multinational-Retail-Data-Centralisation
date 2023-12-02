-- SELECT MAX(length(month)) FROM dim_date_times
ALTER TABLE dim_date_times
	ALTER COLUMN month TYPE VARCHAR(2);

-- SELECT MAX(length(year)) FROM dim_date_times
ALTER TABLE dim_date_times
	ALTER COLUMN year TYPE VARCHAR(4);


-- SELECT MAX(length(day)) FROM dim_date_times
ALTER TABLE dim_date_times
	ALTER COLUMN day TYPE VARCHAR(2);


-- SELECT MAX(length(time_period)) FROM dim_date_times
ALTER TABLE dim_date_times
	ALTER COLUMN time_period TYPE VARCHAR(10);

-- SELECT MAX(length(time_period)) FROM dim_date_times
ALTER TABLE dim_date_times
	ALTER COLUMN date_uuid TYPE UUID
	USING CAST(date_uuid AS UUID);

SELECT * FROM dim_date_times


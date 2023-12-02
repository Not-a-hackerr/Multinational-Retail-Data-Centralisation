-- TASK 7 Staff headcount

SELECT * FROM dim_store_details;

SELECT
	  SUM(dim_store_details.staff_numbers) AS total_stafff_numbers,
	  dim_store_details.country_code
FROM 
	dim_store_details
GROUP BY
	country_code
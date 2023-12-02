-- TASK 1 How many stores in which countries
SELECT * FROM dim_store_details; 


SELECT country_code,
 		COUNT(country_code) AS total_no_stores
FROM 
	dim_store_details
GROUP BY 
	country_code
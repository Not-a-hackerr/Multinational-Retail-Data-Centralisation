-- TASK 2 Which locations currently have the most stores
SELECT * FROM dim_store_details;

SELECT locality,
	COUNT(locality) AS total_no_stores
FROM
	dim_store_details
GROUP BY 
	locality
ORDER BY
	total_no_stores DESC
LIMIT 
	7


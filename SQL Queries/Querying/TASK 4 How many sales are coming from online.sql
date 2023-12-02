-- TASK 4 How many sales are coming from online
SELECT * FROM orders_table;


SELECT 
	COUNT(store_code) AS total_number_of_sales,
	SUM(product_quantity) AS product_quantity_count,
	CASE
		WHEN store_code LIKE '%WEB%' THEN 'WEB'
		ELSE 'Offline'
	END AS location
FROM 
	orders_table
GROUP BY 
	location

-- TASK 3 Months which have produced the largest amount of sales

SELECT 
	(orders_table.product_quantity) * (dim_products.product_price) AS total_sales,
	dim_date_times.month
FROM
	orders_table
JOIN 
	dim_products ON orders_table.product_code = dim_products.product_code
JOIN	
	dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid; 



SELECT 
		ROUND(SUM(total_sales)::numeric, 2) AS total_sales, 
		month 
FROM 	
	(
	SELECT 
		(orders_table.product_quantity) * (dim_products.product_price) AS total_sales,
		dim_date_times.month AS month
	FROM
		orders_table
	JOIN 
		dim_products ON orders_table.product_code = dim_products.product_code
	JOIN	
		dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
	) subquery
	
GROUP BY 
	month
ORDER BY 
	total_sales DESC
LIMIT 
	6
	
	

	
	
-- SELECT * 




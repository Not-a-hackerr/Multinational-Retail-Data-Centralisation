-- TASK 6 Which month in each year produced the highest cost of sales?
SELECT 
	SUM((dim_products.product_price) * (orders_table.product_quantity))::numeric AS total_sales,
	dim_date_times.year AS year,
	dim_date_times.month AS month
FROM
	orders_table
JOIN 
	dim_products ON orders_table.product_code = dim_products.product_code
JOIN	
	dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid

GROUP BY 
	year, month
ORDER BY 
	total_sales DESC
LIMIT 
	10
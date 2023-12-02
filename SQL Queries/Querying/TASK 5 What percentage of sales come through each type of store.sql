-- TASK 5 What percentage of sales come through each type of store

SELECT 
	 store_type,
	 ROUND(SUM(total_sales)::numeric, 2) AS total_sales,
	 ROUND(SUM(total_sales)::numeric / SUM(SUM(total_sales)::numeric) OVER () * 100, 2)  AS "percentage_total(%)"
FROM 
	(
	SELECT 
		dim_store_details.store_type AS store_type,
		(dim_products.product_price) * (orders_table.product_quantity) AS total_sales
	FROM
		orders_table
	JOIN 
		dim_products ON orders_table.product_code = dim_products.product_code
	JOIN	
		dim_store_details ON orders_table.store_code = dim_store_details.store_code
	 )subquery
GROUP BY 
	store_type
ORDER BY 
	total_sales DESC



-- TASK 9 How quickly is the company making sales?

 WITH number_of_orders_by_year AS (
    SELECT
        year,
        COUNT(timestamp) AS number_of_orders
    FROM 
        dim_date_times
    GROUP BY 
        year

),
hours AS (
	SELECT 
		number_of_orders_by_year.year,
		8.760e+3 / number_of_orders AS the_hours
	FROM 
	 number_of_orders_by_year
	),
minutes AS( 
	SELECT
		number_of_orders_by_year.year,
		60 * ( hours.the_hours - FLOOR(hours.the_hours)) AS the_minutes
	FROM
		number_of_orders_by_year,
		hours
),
seconds AS( 
	SELECT
		number_of_orders_by_year.year,
		60 * (minutes.the_minutes - FLOOR(minutes.the_minutes)) AS the_seconds
	FROM
		number_of_orders_by_year,
		minutes
),
-- milliseconds AS( 
-- 	SELECT
-- 		number_of_orders_by_year.year,
-- 		1000 * (seconds.the_seconds - FLOOR(seconds.the_seconds)) AS the_milliseconds
-- 	FROM
-- 		number_of_orders_by_year,
-- 		seconds
-- )


SELECT 
    number_of_orders_by_year.year,
    FLOOR(the_hours) AS hours,
	FLOOR(the_minutes) AS minutes,
	FLOOR(the_seconds) AS seconds
	
FROM 
    number_of_orders_by_year
JOIN
    hours ON number_of_orders_by_year.year = hours.year
JOIN
	minutes ON number_of_orders_by_year.year = minutes.year
JOIN
	seconds ON number_of_orders_by_year.year = seconds.year
-- JOIN
-- 	milliseconds ON number_of_orders_by_year.year = milliseconds.year;


-- TASK 9 How quickly is the company making sales?

WITH date_time AS(
SELECT
	year,
    (year || '-' || LPAD(month::text, 2, '0') || '-' || LPAD(day::text, 2, '0') || ' ' || timestamp)::timestamp AS full_datetime
FROM 
    dim_date_times
),

next_datetime AS (
    SELECT
		year,
        full_datetime,
        LEAD(full_datetime) OVER (ORDER BY full_datetime ASC) AS next_date_time
    FROM
        date_time
),
time_difference_seconds AS (
    SELECT
		year,
        ABS(EXTRACT(EPOCH FROM (next_date_time - full_datetime))) AS time_difference
    FROM
        next_datetime
),
average_time_in_seconds AS (
    SELECT 
        year,
        AVG(time_difference) AS time
    FROM 
        time_difference_seconds
    GROUP BY 
        year
	ORDER BY
		time DESC
)


SELECT 
	year,
	CONCAT('Hours: ', FLOOR(average_time_in_seconds.time / 3600), ', ' ,' Minutes: ', FLOOR(MOD(average_time_in_seconds.time, 3600)/60), 
		   ', ', ' Seconds: ', FLOOR(MOD(average_time_in_seconds.time, 60)) , ', ', 'Milliseconds: ', FLOOR(MOD(average_time_in_seconds.time, 1000))
	)
FROM 
	average_time_in_seconds
LIMIT
	10
		
		




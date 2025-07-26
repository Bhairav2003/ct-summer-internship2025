Weather Observation Station 20 :Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to decimal places.

Answer:
SELECT ROUND(Median_LAT_N, 4) AS Median_LAT_N
FROM (
    SELECT DISTINCT
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY LAT_N) 
        OVER () AS Median_LAT_N
    FROM STATION) AS sub
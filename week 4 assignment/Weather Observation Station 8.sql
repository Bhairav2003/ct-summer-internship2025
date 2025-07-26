--Weather Observation Station 8 : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths

--Answer:

SELECT DISTINCT CITY
FROM   STATION
WHERE  LOWER(LEFT(CITY, 1))  IN ('a','e','i','o','u')   
  AND  LOWER(RIGHT(CITY, 1)) IN ('a','e','i','o','u');
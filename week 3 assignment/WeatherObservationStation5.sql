Weather Observation Station 5 : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths
Resources :
https://www.hackerrank.com/challenges/weather-observation-station-5/problem

Answer:

SELECT TOP 1 CITY,LEN(CITY) AS LENGTH
FROM STATION
ORDER BY LEN(CITY),CITY;

SELECT TOP 1 CITY, LEN(CITY) AS LENGTH
FROM STATION
ORDER BY LEN(CITY) DESC, CITY;
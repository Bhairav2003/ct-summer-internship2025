Weather Observation Station 3 : Query a list of CITY names from STATION for cities that have an even ID number
Resources :
https://www.hackerrank.com/challenges/weather-observation-station-3/problem

Answer:

SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0
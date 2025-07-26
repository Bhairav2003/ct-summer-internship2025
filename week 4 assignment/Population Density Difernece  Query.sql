Population Density Difernece : Query the difference between the maximum and minimum populations in CITY.

Answer:
SELECT MAX(POPULATION) - MIN(POPULATION) AS PopulationDifference
FROM CITY;
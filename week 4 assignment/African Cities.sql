African Cities : Query the names of all cities where the CONTINENT is 'Africa'.

Answer:
SELECT CITY.Name FROM CITY
JOIN COUNTRY
  ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.Continent = 'Africa';
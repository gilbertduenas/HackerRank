/* It's dangerous out there. Don't SQL alone. */

/* https://www.hackerrank.com/challenges/japanese-cities-attributes/problem */
SELECT *
FROM city
WHERE countrycode = 'JPN';


/* https://www.hackerrank.com/challenges/japanese-cities-name/problem */
SELECT name
FROM city
WHERE countrycode = 'JPN';


/* https://www.hackerrank.com/challenges/more-than-75-marks/problem */
SELECT name
FROM students
WHERE marks > 75
ORDER BY SUBSTR(name, -3),
         id;


/* https://www.hackerrank.com/challenges/name-of-employees/problem */
SELECT name
FROM employee
ORDER BY name ASC;


/* https://www.hackerrank.com/challenges/revising-the-select-query/problem */
SELECT *
FROM city
WHERE countrycode = 'USA'
  AND population > 100000;


/* https://www.hackerrank.com/challenges/revising-the-select-query-2/problem */
SELECT name
FROM city
WHERE countrycode = 'USA'
  AND population > 120000;


/* https://www.hackerrank.com/challenges/salary-of-employees/problem */
SELECT name
FROM employee
WHERE months < 10
  AND salary > 2000
ORDER BY employee_id;


/* https://www.hackerrank.com/challenges/select-all-sql/problem */
SELECT *
FROM city;


/* https://www.hackerrank.com/challenges/select-by-id/problem */
SELECT *
FROM city
WHERE id = 1661;


/* https://www.hackerrank.com/challenges/weather-observation-station-1/problem */
SELECT city,
       state
FROM station;


/* https://www.hackerrank.com/challenges/weather-observation-station-2/problem */
SELECT ROUND(SUM(lat_n), 2),
       ROUND(SUM(long_w), 2)
FROM station;


/* https://www.hackerrank.com/challenges/weather-observation-station-3/problem */
SELECT DISTINCT city
FROM station
WHERE id%2 LIKE 0;


/* https://www.hackerrank.com/challenges/weather-observation-station-4/problem */
SELECT COUNT(city) - COUNT(DISTINCT city)
FROM station;


/* https://www.hackerrank.com/challenges/weather-observation-station-5/problem */
SELECT city,
       MIN(CHAR_LENGTH(city))
FROM station
GROUP BY city
ORDER BY CHAR_LENGTH(city),
         city
LIMIT 1;

SELECT city,
       MAX(CHAR_LENGTH(city))
FROM station
GROUP BY city
ORDER BY CHAR_LENGTH(city) DESC, city ASC
LIMIT 1;


/* https://www.hackerrank.com/challenges/weather-observation-station-6/problem */
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[AEIOU].*';


/* https://www.hackerrank.com/challenges/weather-observation-station-7/problem */
SELECT DISTINCT city
FROM station
WHERE city REGEXP '[AEIOU]$';


/* https://www.hackerrank.com/challenges/weather-observation-station-8/problem */
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[AEIOU].*[AEIOU]$';


/* https://www.hackerrank.com/challenges/weather-observation-station-9/problem */
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '^[AEIOU].*';


/* https://www.hackerrank.com/challenges/weather-observation-station-10/problem */
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '[AEIOU]$';


/* https://www.hackerrank.com/challenges/weather-observation-station-11/problem */
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '^[AEIOU].*[AEIOU]$';


/* https://www.hackerrank.com/challenges/weather-observation-station-12/problem */
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[^AEIOU].*[^AEIOU]$';

/**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**/
/**/   /**/  /**/  /**//**/ /**//**/ /**/    /**//**/ /**/    /**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**/
/**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**/
/**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**/
/**//**//**//**//**//**//**//**//**//**//**/
          /**/             /**//**//**//**//**//**//**//**//**/
/**//**//**//**//**/
/**/              /**/         /**//**//**//**/
/**//**//**//**//**//**/
/**//**//**//**//**//**//**//**/
/**//**//**//**/
/**//**//**//**/
          /**/             /**//**//**/
/**//**//**/
/**/                       /**/
/**//**//**/
          /**/     /**/        /**//**//**//**//**//**//**/
/**//**//**//**//**/
/**//**//**//**//**//**/
/**//**//**//**/
               /**/        /**//**/
/**//**/
/**//**//**//**/
/**//**//**//**/
/**//**//**//**//**//**//**//**//**//**/
/**//**//**//**//**/
/**//**/
/**/ /**//**//**//**//**/
/**//**//**/

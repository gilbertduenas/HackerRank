/* https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem */
/*************************************************************************/


/* https://www.hackerrank.com/challenges/interviews/problem */
/************************************************************/


/* https://www.hackerrank.com/challenges/placements/problem */
/************************************************************/
SELECT S.name
FROM (students S
      JOIN friends F USING(id)
      JOIN packages SP ON S.id = SP.id
      JOIN packages FP ON F.friend_id = FP.id)
WHERE SP.salary < FP.salary
ORDER BY FP.salary;


/* https://www.hackerrank.com/challenges/sql-projects/problem */
/**************************************************************/
SELECT start_date,
       MIN(end_date)
FROM
  (SELECT start_date
   FROM projects
   WHERE start_date NOT IN
       (SELECT end_date
        FROM projects)) starts,

  (SELECT end_date
   FROM projects
   WHERE end_date NOT IN
       (SELECT start_date
        FROM projects)) ends
WHERE start_date < end_date
GROUP BY start_date
ORDER BY DATEDIFF(start_date, MIN(end_date)) DESC, start_date;


/* https://www.hackerrank.com/challenges/symmetric-pairs/problem */
/*****************************************************************/
SELECT f1.x,
       f1.y
FROM functions f1
JOIN functions f2 ON f1.x = f2.y
AND f1.y = f2.x
GROUP BY f1.x,
         f1.y
HAVING COUNT(f1.x) > 1
OR f1.x < f1.y
ORDER BY f1.x;


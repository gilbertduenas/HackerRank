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


/* https://www.hackerrank.com/challenges/symmetric-pairs/problem */
/*****************************************************************/


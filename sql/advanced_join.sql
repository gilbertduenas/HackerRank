/* https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem */
SELECT submission_date,
  (SELECT COUNT(DISTINCT hacker_id)
   FROM submissions s1
   WHERE s1.submission_date = s2.submission_date
     AND
       (SELECT COUNT(DISTINCT s3.submission_date)
        FROM submissions s3
        WHERE s3.hacker_id = s1.hacker_id
          AND s3.submission_date < s2.submission_date) = dateDIFF(s2.submission_date, '2016-03-01')),
  (SELECT hacker_id
   FROM submissions s1
   WHERE s1.submission_date = s2.submission_date
   GROUP BY hacker_id
   ORDER BY count(submission_id) DESC, hacker_id
   LIMIT 1) H_ID,
  (SELECT name
   FROM hackers
   WHERE hacker_id = H_ID)
FROM
  (SELECT DISTINCT submission_date
   FROM submissions) s2
GROUP BY submission_date;
 

/* https://www.hackerrank.com/challenges/interviews/problem */
SELECT C.contest_id,
       C.hacker_id,
       C.name,
       SUM(ts_sum),
       SUM(tas_sum),
       SUM(tv_sum),
       SUM(tuv_sum)
FROM contests C
JOIN colleges U ON C.contest_id = U.contest_id
JOIN challenges H ON U.college_id = H.college_id
LEFT JOIN
  (SELECT VS.challenge_id,
          SUM(VS.total_views) tv_sum,
          SUM(VS.total_unique_views) tuv_sum
   FROM view_stats VS
   GROUP BY VS.challenge_id) V ON H.challenge_id = V.challenge_id
LEFT JOIN
  (SELECT SS.challenge_id,
          SUM(SS.total_submissions) ts_sum,
          SUM(SS.total_accepted_submissions) tas_sum
   FROM submission_stats SS
   GROUP BY SS.challenge_id) S ON H.challenge_id = S.challenge_id
GROUP BY C.contest_id,
         C.hacker_id,
         C.name
HAVING SUM(ts_sum) + SUM(tas_sum) + SUM(tv_sum) + SUM(tuv_sum) > 0
ORDER BY C.contest_id;


/* https://www.hackerrank.com/challenges/placements/problem */
SELECT S.name
FROM (students S
      JOIN friends F USING(id)
      JOIN packages SP ON S.id = SP.id
      JOIN packages FP ON F.friend_id = FP.id)
WHERE SP.salary < FP.salary
ORDER BY FP.salary;


/* https://www.hackerrank.com/challenges/sql-projects/problem */
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

       /**//**//**/            /**/     /**/         /**/
/**//**/
/**//**//**/
/**/
/**/
/**//**//**//**/
                                  
/**//**/
/**/
/**/
/**//**//**/
/**//**/
                          /**/        
/**//**//**//**/
/**/
/**//**/

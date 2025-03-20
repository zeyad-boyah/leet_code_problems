"""
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.
"""


SELECT id
FROM (
    SELECT id,
           CASE 
               WHEN DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) >=2  THEN 0
               WHEN LAG(temperature) OVER (ORDER BY recordDate) < temperature THEN 1
               ELSE 0
           END AS is_higher
    FROM Weather
) AS subquery
WHERE is_higher = 1;
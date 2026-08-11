-- Last updated: 8/11/2026, 4:05:51 PM
# Write your MySQL query statement below
SELECT s.product_id,
       s.year AS first_year,
       s.quantity,
       s.price
FROM Sales s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) t
ON s.product_id = t.product_id
AND s.year = t.first_year;
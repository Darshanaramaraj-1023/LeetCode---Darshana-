-- Last updated: 8/11/2026, 4:11:20 PM
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
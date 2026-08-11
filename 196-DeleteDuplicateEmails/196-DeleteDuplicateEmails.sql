-- Last updated: 8/11/2026, 4:10:58 PM
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;
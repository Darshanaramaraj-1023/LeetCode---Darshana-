-- Last updated: 8/11/2026, 4:08:15 PM
SELECT name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;
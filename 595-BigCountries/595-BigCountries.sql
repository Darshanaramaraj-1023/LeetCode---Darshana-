-- Last updated: 8/11/2026, 4:08:08 PM
SELECT
    name,
    population,
    area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
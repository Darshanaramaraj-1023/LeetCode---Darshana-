-- Last updated: 8/11/2026, 4:11:30 PM
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
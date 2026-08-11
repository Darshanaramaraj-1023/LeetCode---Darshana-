-- Last updated: 8/11/2026, 4:05:42 PM
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
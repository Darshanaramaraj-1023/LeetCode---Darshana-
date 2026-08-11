-- Last updated: 8/11/2026, 4:08:22 PM
# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN Employee emp
ON e.id = emp.managerId
GROUP BY e.id, e.name
HAVING COUNT(emp.id) >= 5;
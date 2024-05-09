-- May 9, 2024
-- Status: Complete
-- Notes: Was not easy. Had to use solutions. Should come back to this.

SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;

-- can also use DATEDIFF(w1.recordDatem w2.recordDate) = 1
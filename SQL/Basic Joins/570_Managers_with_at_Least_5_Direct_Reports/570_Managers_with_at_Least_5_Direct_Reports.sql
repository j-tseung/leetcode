-- May 9, 2024
-- Status: Complete
-- Notes:  

SELECT 
    E1.name
FROM 
    Employee AS E1
JOIN
    Employee AS E2 ON E1.id = E2.managerId
GROUP BY 
    E1.id
HAVING
    COUNT(E2.managerId) >= 5

-- May 3, 2024
-- Status: Ongoing
-- Notes: 

SELECT Visits.customer_id, count_no_trans
FROM Visits
OUTER JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE 

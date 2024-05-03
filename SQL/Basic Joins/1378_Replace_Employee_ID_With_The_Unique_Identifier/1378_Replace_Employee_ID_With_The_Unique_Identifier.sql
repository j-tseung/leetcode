-- May 3, 2024
-- Status: Complete
-- Notes: Learned LEFT JOIN, RIGHT JOIN, JOIN

SELECT EmployeeUNI.unique_id, Employees.name
FROM EmployeeUNI
RIGHT JOIN Employees ON EmployeeUNI.id = Employees.id;


-- SELECT Employees.name, EmployeeUNI.unique_id
-- FROM Employees
-- LEFT JOIN EmployeeUNI ON EmployeeUNI.id = Employees.id;

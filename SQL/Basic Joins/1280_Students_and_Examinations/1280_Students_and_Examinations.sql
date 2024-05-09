-- May 9, 2024
-- Status: Complete
-- Notes: Needed hints to get to CROSS JOIN. 

SELECT
    St.student_id,
    St.student_name,
    Su.subject_name,
    COUNT(E.student_id) AS attended_exams
FROM 
    Students AS St
CROSS JOIN 
    Subjects AS Su
LEFT JOIN 
    Examinations AS E ON St.student_id = E.student_id AND Su.subject_name = E.subject_name
GROUP BY   
    St.student_id, St.student_name, Su.subject_name  -- Ensures aggregation is done for each student-subject pair
ORDER BY 
    St.student_id ASC, Su.subject_name ASC;

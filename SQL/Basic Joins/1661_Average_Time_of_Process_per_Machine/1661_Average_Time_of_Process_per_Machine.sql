-- May 9, 2024
-- Status: Ongoing
-- Notes: If we substract the sum of all start timestamps from the sum of all end 
-- timestamps we'll get the total time the machine spent on all processes.

-- solution taken from editorial
SELECT a.machine_id, 
       ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a, 
     Activity b
WHERE 
    a.machine_id = b.machine_id
AND 
    a.process_id = b.process_id
AND 
    a.activity_type = 'start'
AND 
    b.activity_type = 'end'
GROUP BY machine_id
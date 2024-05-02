-- May 2, 2024
-- Status: Complete
-- Notes: Learned "DISTINCT" and "SORT BY" 
-- 


SELECT DISTINCT author_id AS id
FROM Views 
WHERE author_id = viewer_id
ORDER BY id ASC;
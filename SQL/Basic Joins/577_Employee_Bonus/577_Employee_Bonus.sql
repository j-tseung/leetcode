-- May 9, 2024
-- Status: Complete
-- Notes: :tada: The first join one I ever completely did myself. 

select E.name, B.bonus
from Employee as E
left join Bonus as B on E.empId = B.empID
where B.bonus < 1000 or B.bonus is null;
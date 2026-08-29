Select employee_id, Case 
            when employee_id % 2 != 0 and name not like 'M%' 
                Then salary
            Else 0 
            End
            as bonus
from employees
order by employee_id
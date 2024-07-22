# Write your MySQL query statement below
with rnks as (select
id,
name,
salary,
departmentId,
dense_rank() over (partition by departmentId order by salary desc) as rnk
from employee),

filter as (select
departmentId,
name,
salary 
from rnks
where rnk<=3)

select
d.name as Department,
f.name as Employee,
f.salary as Salary
from
filter f
left join
department d
on f.departmentId=d.id
# Write your MySQL query statement below
# select salary as SecondHighestSalary from (
# select *
# from employee
# order by salary desc
# limit 2,2) a
# order by salary asc
# limit 1

select
max(salary) as SecondHighestSalary
from employee
where salary<(Select max(salary) from employee)

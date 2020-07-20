'''
编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
通过次数116,685提交次数331,413
链接：https://leetcode-cn.com/problems/second-highest-salary
'''
'''
ifnull(x，y)，若x不为空则返回x，否则返回y，这道题y=null
mysql 的 limit N，M
    M 表示在限制条数之后的offset条记录。
distinct，过滤关键字
select 
ifnull
(
    (select distinct Salary
    from Employee
    order by Salary desc
    limit 1,1),
    null
)as 'SecondHighestSalary'
'''

# 使用ifnull
'''
select IFNULL((select distinct(Salary) 
from Employee
order by Salary desc
limit 1,1),null) as SecondHighestSalary
'''
# 使用max
'''
select max(Salary) as SecondHighestSalary
from employee
where
salary<(select max(salary) from employee)
'''
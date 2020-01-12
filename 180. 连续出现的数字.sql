180. 连续出现的数字.sql
'''
编写一个 SQL 查询，查找所有至少连续出现三次的数字。

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

链接：https://leetcode-cn.com/problems/consecutive-numbers
'''

思路一：
然后我们从上表中选择任意的 Num 获得想要的答案。同时我们需要添加关键字 DISTINCT ，因为如果一个数字连续出现超过 3 次，会返回重复元素。

MySQL

方法：用 DISTINCT 和 WHERE 语句
算法

连续出现的意味着相同数字的 Id 是连着的，由于这题问的是至少连续出现 3 次，我们使用 Logs 并检查是否有 3 个连续的相同数字。
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;

思路二：
-- 思路用2个变量统计。pre变量统计上一次Num，cnt统计连续次数
# Write your MySQL query statement below
'''
语法解释：

IF(expr1,  expr2, expr3) //三元表达式
@pre:=10 // 变量赋值语法
使用select 语句设置变量，可看做表，在datagrip中直接运行可以显示为表 pre ==> 记录上一个值， cnt ==> 记录次数，

select @pre:=null,  @cnt:=0 
如果pre与t.num 相等，则cnt加1， 否则cnt重置为1

 @cnt:=IF(@pre=t.Num, @cnt+1, 1) cnt
将生成的num与cnt次数的表，作为新的表 a

SELECT t.Num ,
       @cnt:=IF(@pre=t.Num, @cnt+1, 1) cnt,
       @pre:=t.Num pre
  FROM Logs t, (SELECT @pre:=null, @cnt:=0) b) a
'''
SELECT DISTINCT a.Num ConsecutiveNums FROM (
SELECT t.Num ,
       @cnt:=IF(@pre=t.Num, @cnt+1, 1) cnt,
       @pre:=t.Num pre
  FROM Logs t, (SELECT @pre:=null, @cnt:=0) b) a
  WHERE a.cnt >= 3
'''
小美是一所中学的信息科技老师，她有一张 seat 座位表，平时用来储存学生名字和与他们相对应的座位 id。

其中纵列的 id 是连续递增的

小美想改变相邻俩学生的座位。

你能不能帮她写一个 SQL query 来输出小美想要的结果呢？

 

示例：

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
假如数据输入的是上表，则输出结果如下：

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
注意：

如果学生人数是奇数，则不需要改变最后一个同学的座位。
'''
SELECT id, (id + 1) ^ 1 - 1, student FROM seat;

| id | (id+1)^1-1 | student |
|----|------------|---------|
| 1  | 2          | Abbot   |
| 2  | 1          | Doris   |
| 3  | 4          | Emerson |
| 4  | 3          | Green   |
| 5  | 6          | Jeames  |




-- hive
SELECT RANK() OVER(ORDER BY (id - 1) ^ 1) AS id, student FROM seat



-- 异或运算
SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;



-- 窗口查询
# Write your MySQL query statement below
select
    t.id,
    (case when t.num%2 = 1 then t.nextStudent else  t.firstStudent end )as student
from
(
    select
        row_number() over (order by id) as num,
        lag(student,1, student) over (order by id) as 'firstStudent',
        lead(student,1, student) over (order by id) as 'nextStudent',
        id,student
    from seat
) t



-- case when方法
# Write your MySQL query statement below
select
    (case
        when mod(id, 2) = 1 and id != (select max(id) from seat) then id + 1
        when mod(id, 2) = 0 then id - 1
    else id end) as id,
    student
from seat
order by id asc


-- 异或
SELECT b.id, a.student FROM
seat AS a, seat AS b, (SELECT count(*) AS cnt FROM seat) AS c
WHERE b.id = 1 ^ (a.id - 1) + 1
-- where a.id=1^(b.id-1)+1; 也可以这样写，更容易理解
 || (c.cnt % 2 && b.id = c.cnt && a.id = c.cnt);

-- 排序
SELECT IF(id % 2 = 0, id - 1, IF(id = cnt, id, id + 1)) AS id, s tudent
    FROM (SELECT count(*) as cnt FROM seat) AS a, seat ORDER BY id;



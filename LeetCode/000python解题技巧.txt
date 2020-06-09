# 000python解题技巧.py

1.
python中取数
'''
需要注意的一点就是，python的取模是根据向下取整法的，而c/c++/java是基于向零取整的。
例如：
在python中 ：-53除以10=-6 …7 所以python中 -53%10=7
在c语言中，-53除以10=-5 … -3 所以c语言中 -53%10=-3
（python3中， /是精确除法，//是向下取整除法，%是求模，四舍五入取整round, 向零取整int, 向下和向上取整函数math.floor, math.ceil）
'''
2.
Counter（计数器）：用于追踪值的出现次数为dict
'''
from collection import Counter

Counter类继承dict类，所以它能使用dict类里面的方法 
import collections
obj = collections.Counter('aabbccc')
print(obj)

#输出：Counter({'c': 3, 'a': 2, 'b': 2})
'''
3.
bisect
import bisect

L = [1, 3, 3, 6, 8, 12, 15]
x = 3

x_insert_point = bisect.bisect_left(L, x)　　  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回左侧位置１

x_insert_point = bisect.bisect_right(L, x)  # 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回右侧位置３

x_insort_left = bisect.insort_left(L, x)  # 将x插入到列表L中，x存在时插入在左侧

x_insort_rigth = bisect.insort_right(L, x)  # 将x插入到列表L中，x存在时插入在右侧　

4.
defaultdict
from collections import defaultdict

a = defaultdict(int)

5.
zip
和 * zip
'''
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]

nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)

输出结果：
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')
'''

6.
自定义排序
import functools
list.sort(key=functools.cmp_to_key(sort1))
def sort1(a,b):
	return b[1] - a[1] if a[0] == b[0] else a[0] - b[0]

# 如下也可以做到 相当于传一个tuple进行比较，按第一个元素升序，第二个元素降序 相当于Scala中的自定义排序 sortBy
arr.sort(key=lambda x: (x[0], -x[1]))

7.count函数====>该方法返回子字符串在字符串中出现的次数。

	s = "aaaacc"
	c = min(set(s), key=s.count)
	print(c)

描述
Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

语法
count()方法语法：

str.count(sub, start= 0,end=len(string))
参数
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

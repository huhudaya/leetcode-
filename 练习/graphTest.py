# 图的表示方法有两种，邻结矩阵和散列表
'''
图解算法中的BFS算法的思想
1.创建一个队列，将要查找的人添加到队列中（先添加一度关系的）
2.从队列弹出一个人
3.检查判断是否找到，找到了即退出
4.没有找到就将这个人的朋友都添加到这个队列中（二度关系）

很重要的是：检查一个人之前，必须判断之前有没有检查过他，我们可以用一个列表来记录检查过的人
'''

from collections import deque
graph = {}
def search(name):
    search_queue = deque()
    search_queue += graph["name"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("has seen")
                return True
            else:
                # 这里的图用邻接矩阵表示！这里的graph[person]是一个列表
                search_queue += (graph[person])
                searched.append(person)

def person_is_seller(person):
    pass



# 注意 树是一种特殊的图

a = deque()
a.append(0)
b = [1,2,3]
a.extend(b)
print(a)



# 迪克斯特拉算法
'''
1.找出最便宜的节点，即可以在最短时间内前往的节点
2.对于该点的邻居，检查是否有前往它们更短的路径，
'''
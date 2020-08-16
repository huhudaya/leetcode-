'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n
你需要让组成和的完全平方数的个数最少

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''


class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        deq = deque()
        visited = set()

        deq.append((n, 0))
        while deq:
            number, step = deq.popleft()
            targets = [number - i * i for i in range(1, int(number ** 0.5) + 1)]
            for target in targets:
                if target == 0:
                    return step + 1
                if target not in visited:
                    deq.append((target, step + 1))
                    visited.add(target)
        return 0

# Java
'''
class Solution {
    public int numSquares(int n) {
        Queue<Integer> queue = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();
        int level = 0;
        queue.add(n);
        while (!queue.isEmpty()) {
            int size = queue.size();
            level++; // 开始生成下一层
            for (int i = 0; i < size; i++) {
                int cur = queue.poll();
                //依次减 1, 4, 9... 生成下一层的节点
                for (int j = 1; j * j <= cur; j++) {
                    int next = cur - j * j;
                    if (next == 0) {
                        return level;
                    }
                    if (!visited.contains(next)) {
                        queue.offer(next);
                        visited.add(next);
                    }
                }
            }
        }
        return -1;
    }
}
'''

# 自己的版本
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        # BFS
        seen = set()
        queue = deque()
        queue.append(n)
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for i in range(size):
                cur = queue.popleft()
                #  依次减 1, 4, 9... 生成下一层的节点
                j = 1
                while j ** 2 <= cur:
                    nxt = cur - j * j
                    j += 1
                    if nxt == 0:
                        return level
                    if nxt not in seen:
                        queue.append(nxt)
                        seen.add(nxt)
        return -1
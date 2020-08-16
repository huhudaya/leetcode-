'''

有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

示例 1:

输入:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。
注意:

image 和 image[0] 的长度在范围 [1, 50] 内。
给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
通过次数30,038提交次数52,491
'''
# java
'''
class Solution {
    int[] dx = {1, 0, 0, -1};
    int[] dy = {0, 1, -1, 0};

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int currColor = image[sr][sc];
        if (currColor == newColor) {
            return image;
        }
        int n = image.length, m = image[0].length;
        Queue<int[]> queue = new LinkedList<int[]>();
        queue.offer(new int[]{sr, sc});
        image[sr][sc] = newColor;
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0], y = cell[1];
            for (int i = 0; i < 4; i++) {
                int mx = x + dx[i], my = y + dy[i];
                if (mx >= 0 && mx < n && my >= 0 && my < m && image[mx][my] == currColor) {
                    queue.offer(new int[]{mx, my});
                    image[mx][my] = newColor;
                }
            }
        }
        return image;
    }
}
'''
from typing import List
import collections


# DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # DFS(递归)
        color = image[sr][sc]
        if newColor == color:
            return image
        height, width = len(image), len(image[0])
        distance = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def helper(x, y):
            if image[x][y] == color:
                image[x][y] = newColor
                for dis in distance:
                    a, b = x + dis[0], y + dis[1]
                    if 0 <= a < height and 0 <= b < width:
                        helper(a, b)

        helper(sr, sc)
        return image


# DFS用栈
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # DFS(迭代)
        color = image[sr][sc]
        if newColor == color:
            return image
        height, width = len(image), len(image[0])
        distance = ((-1, 0), (1, 0), (0, -1), (0, 1))
        stack = [(sr, sc)]
        while stack:
            x, y = stack.pop()
            image[x][y] = newColor
            for dis in distance:
                a, b = x + dis[0], y + dis[1]
                if 0 <= a < height and 0 <= b < width and image[x][y] == color:
                    stack.append((a, b))
        return image


# BFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # BFS
        color = image[sr][sc]
        if newColor == color:
            return image
        height, width = len(image), len(image[0])
        distance = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = collections.deque([(sr, sc)])
        while queue:
            x, y = queue.popleft()
            image[x][y] = newColor
            for dis in distance:
                a, b = x + dis[0], y + dis[1]
                if 0 <= a < height and 0 <= b < width and image[a][b] == color:
                    queue.append((a, b))
        return image

# 59. 螺旋矩阵 II.py
'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

链接：https://leetcode-cn.com/problems/spiral-matrix-ii
'''
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
    	# 左 右 上 下 四条边
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat
# java
'''
class Solution {
    public int[][] generateMatrix(int n) {
        int l = 0, r = n - 1, t = 0, b = n - 1;
        int[][] mat = new int[n][n];
        int num = 1, tar = n * n;
        while(num <= tar){
            for(int i = l; i <= r; i++) mat[t][i] = num++; // left to right.
            t++;
            for(int i = t; i <= b; i++) mat[i][r] = num++; // top to bottom.
            r--;
            for(int i = r; i >= l; i--) mat[b][i] = num++; // right to left.
            b--;
            for(int i = b; i >= t; i--) mat[i][l] = num++; // bottom to top.
            l++;
        }
        return mat;
    }
}
'''
# 模拟过程
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[False]*n for _ in range(n)]
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        x,y=0,0
        count=0
        
        for i in range(1,n*n+1):
            res[x][y]=i
            dir_x,dir_y=directions[count][0],directions[count][1]
            if(0<=x+dir_x<n and 0<=y+dir_y<n and not res[x+dir_x][y+dir_y]):
                x=x+dir_x
                y=y+dir_y
            else:
                count=(count+1)%4
                x=x+directions[count][0]
                y=y+directions[count][1]
        return res

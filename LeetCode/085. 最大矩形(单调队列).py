# 85. 最大矩形.py

# 暴力法
'''
class Solution {
public:
    int maximalRectangle(vector<vector<char> > &matrix) {
        int num_i=matrix.size();
        if (num_i==0) return 0;
        int num_j=matrix[0].size();
        if (num_j==0) return 0;
        vector<vector<int>> max_x(num_i,vector<int>(num_j,0));  //number of consecutive 1s to the left of matrix[i][j], including itself
        int area=0;
        for (int i=0;i<num_i;i++){
            for (int j=0;j<num_j;j++){
                if (matrix[i][j]=='1'){
                    if (j==0) max_x[i][j]=1;
                    else max_x[i][j]=max_x[i][j-1]+1;
                    int y=1;
                    int x=num_j;
                    while((i-y+1>=0)&&(matrix[i-y+1][j]=='1')){
                        x=min(x, max_x[i-y+1][j]);
                        area=max(area,x*y);
                        y++;
                    } 
                }
            }
        }
        return area;
    }
};
# 暴力法
public int maximalRectangle(char[][] matrix) {
    if (matrix.length == 0) {
        return 0;
    }
    //保存以当前数字结尾的连续 1 的个数
    int[][] width = new int[matrix.length][matrix[0].length];
    int maxArea = 0;
    //遍历每一行
    for (int row = 0; row < matrix.length; row++) {
        for (int col = 0; col < matrix[0].length; col++) {
            //更新 width
            if (matrix[row][col] == '1') {
                if (col == 0) {
                    width[row][col] = 1;
                } else {
                    width[row][col] = width[row][col - 1] + 1;
                }
            } else {
                width[row][col] = 0;
            }
            //记录所有行中最小的数
            int minWidth = width[row][col];
            //向上扩展行
            for (int up_row = row; up_row >= 0; up_row--) {
                int height = row - up_row + 1;
                //找最小的数作为矩阵的宽
                minWidth = Math.min(minWidth, width[up_row][col]);
                //更新面积
                maxArea = Math.max(maxArea, height * minWidth);
            }
        }
    }
    return maxArea;
}
'''

'''
public int maximalRectangle(char[][] matrix) {
    if (matrix.length == 0) {
        return 0;
    }
    int[] heights = new int[matrix[0].length];
    int maxArea = 0;
    for (int row = 0; row < matrix.length; row++) {
        //遍历每一列，更新高度
        for (int col = 0; col < matrix[0].length; col++) {
            if (matrix[row][col] == '1') {
                heights[col] += 1;
            } else {
                heights[col] = 0;
            }
        }
        //调用上一题的解法，更新函数
        maxArea = Math.max(maxArea, largestRectangleArea(heights));
    }
    return maxArea;
}

public int largestRectangleArea(int[] heights) {
    int maxArea = 0;
    Stack<Integer> stack = new Stack<>();
    int p = 0;
    while (p < heights.length) {
        //栈空入栈
        if (stack.isEmpty()) {
            stack.push(p);
            p++;
        } else {
            int top = stack.peek();
            //当前高度大于栈顶，入栈
            if (heights[p] >= heights[top]) {
                stack.push(p);
                p++;
            } else {
                //保存栈顶高度
                int height = heights[stack.pop()];
                //左边第一个小于当前柱子的下标
                int leftLessMin = stack.isEmpty() ? -1 : stack.peek();
                //右边第一个小于当前柱子的下标
                int RightLessMin = p;
                //计算面积
                int area = (RightLessMin - leftLessMin - 1) * height;
                maxArea = Math.max(area, maxArea);
            }
        }
    }
    while (!stack.isEmpty()) {
        //保存栈顶高度
        int height = heights[stack.pop()];
        //左边第一个小于当前柱子的下标
        int leftLessMin = stack.isEmpty() ? -1 : stack.peek();
        //右边没有小于当前高度的柱子，所以赋值为数组的长度便于计算
        int RightLessMin = heights.length;
        int area = (RightLessMin - leftLessMin - 1) * height;
        maxArea = Math.max(area, maxArea);
    }
    return maxArea;
}
链接：https://leetcode-cn.com/problems/maximal-rectangle/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-8/
'''



# py
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        maxArea = 0
        heigh = [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heigh[j] += 1
                else:
                    heigh[j] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heigh))
        return maxArea
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights is None or len(heights) == 0:
            return 0
        # 单调栈 min
        stack = []
        maxArea = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                curArea = (i - k - 1) * heights[j]
                maxArea = max(maxArea, curArea)
            stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            curArea = (n - k - 1) * heights[j]
            maxArea = max(maxArea, curArea)
        return maxArea
                



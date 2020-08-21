'''
给定一个整数数组，编写一个函数，找出索引m和n
只要将索引区间[m,n]的元素排好序，整个数组就是有序的。
注意：n-m尽量最小，也就是说，找出符合条件的最短序列。
函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。

示例：
输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
输出： [3,9]
提示：
0 <= len(array) <= 1000000
'''
'''
默认升序（降序也只是改一点代码，不影响）
原理：如果左侧最大值大于中间的最小值，则一定会被中间序列包括；
同理，如果右侧最小值大于中间的最大值，则一定会被中间序列包括。

一遍遍历 + 两个指针（两次扫描可一次遍历完成）
    1、从前向后扫描数组，判断当前array[i]是否比max小，是则将last置为当前array下标i，否则更新max;
    2、从后向前扫描数组，判断当前array[len - 1 - i]是否比min大，是则将first置位当前下标len - 1 - i，否则更新min;
    3、返回{first， last}
'''
# Java
'''
class Solution {
    public int[] subSort(int[] array) {
        if(array == null || array.length == 0) return new int[]{-1, -1};
        int last = -1, first = -1;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int len = array.length;
        for(int i = 0; i < len; i++){
            if(array[i] < max){
                last = i;
            }else{
                max = Math.max(max, array[i]);
            }

            if(array[len - 1 - i] > min){
                first = len - 1 - i;
            }else{
                min = Math.min(min, array[len - 1 - i]);
            }
        }
        return new int[] {first, last};
    }
}
'''

# 单调栈Java
'''
class Solution {
    public int[] subSort(int[] array) {
        int len = array.length;
        int[] res = new int[]{-1, -1};
        if (len < 2) return res;
        LinkedList<Integer> stack1 = new LinkedList<>(), stack2 = new LinkedList<>();
        for (int i = 0; i < len; ++i) {
            while (!stack1.isEmpty() && array[stack1.peek()] > array[i])
                stack1.poll();
            stack1.push(i);
            while (!stack2.isEmpty() && array[stack2.peek()] < array[len - 1 - i])
                stack2.poll();
            stack2.push(len - 1 - i);
        }
        if (len == stack1.size()) return res;
        int idx = -1;
        while (!stack1.isEmpty())
            if (stack1.removeLast() != ++idx) {
                res[0] = idx;
                break;
            }
        idx = len;
        while (!stack2.isEmpty())
            if (stack2.removeLast() != --idx) {
                res[1] = idx;
                break;
            }
        return res;
    }
}
'''


# 别的思路
'''
思路1:
1.将数组排序
2.跟原数组左右比较,直到第一个出现不一样的地方即为要调整的开始和结束
例如:
原数组
[1,3,2,6,5,9]
排序后数组
[1,2,3,5,6,9]
左边第一个不一致的index为1,右边第一个不一致的index为4
则结果为[1,4]

思路2:
该思路是思路1的衍生
思路1的实质是找到左右两侧已经按顺序排好的部分,其余则是需要排的.
2遍循环,从左往右找到9是排好的,从右往左找到1是排好的,则结果也是[1,4]
'''
# Java
'''
class Solution {
    public int[] subSort(int[] array) {
        if (array == null || array.length == 0) return new int[]{-1, -1};

        int max = array[0];
        int i = 0;
        int right = -1;
        while (i < array.length) {
            int temp = array[i];
            if (temp < max) right = i;
            max = Math.max(max, temp);
            i++;
        }

        int min = array[array.length-1];
        int j = array.length-1;
        int left = -1;
        while (j >= 0) {
            int temp = array[j];
            if (temp > min) left = j;
            min = Math.min(min, temp);
            j--;
        }

        return new int[]{left, right};
    }
}
'''
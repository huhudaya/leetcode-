'''
给定两个等长数组y[N];A[N]，编程实现如下效果：
其中y中元素为正整数1-50，A中元素为实数-10000-10000，各自数组中都有可能出现重复的数值
选取一组下标集合 {0，1，2.。。。N-1}，使得子数组Y’的不同元素计数乘以数组A'元素之和的值最大，输出最大值。
即使得count(distinct Y[I])乘以sum[A(i)]最大



作业帮二面代码题：
问题：给定两个等长度的一维数组Y[N]和A[N]，编程实现如下效果
其中Y中元素为正整数1-50，A中元素为实数-10000-10000，各自都可能出现重复的数值。
选取一组下标集合{0,1,2,...,N-1}，可能不选取。使得子数组Y'的不同元素计数 乘以 数组A'元素之和 的值最大，输出最大值。
使得count(distinct Y[i]) * sum(A[i])最大，输出最大值

举例说明：
假如Y：{1，2，3} A：{7，4，-1}
1
最大结果：（7+4-1）*count(distinct（1，2，3）)=30
假如Y：{1，1，1, 5, 5, 4} A：{4，-7，4, 4, 1}
1
最大结果：（4+4+1）*count(distinct（5，5，4）)=18

'''

'''
/**
 * 暴力遍历每一个Index记录最大值
 * @param arrA
 * @param arrY
 * @return
 */
private static int getRes(int[] arrA,int[] arrY){
    int max=0;
    for (int i = 0; i < arrA.length; i++) {
        int[] resA=getsubArrSum(arrA,i);
        int[] counts=CountOfdistinctsubArrY(arrY,i);
        for (int j = 0; j <resA.length ; j++) {
            max=Math.max(max,resA[j]*counts[j]);
        }
    }
    return max;
}
/**
 * 记录以arrA[index]到最后   这个子数组中累加和
 * 如当arrA=[1,1,5,-7,4] ，index=0; -->返回的结果为：[1,2,7,0,4]
 * 如当arrA=[1,1,5,-7,4] ，index=1; -->返回的结果为：[1,6,-1,3]
 * @param arrA
 * @param index
 * @return
 */
private static int[] getsubArrSum(int[] arrA,int index){
    int[] res = new int[arrA.length - index];
    if(arrA==null||arrA.length==0){
        return res ;
    }
    for (int i = index; i < arrA.length ; i++) {
        if(i==index){
            res[0]=arrA[index];
        }else {
            res[i-index]=arrA[i]+res[i-index-1];
        }
    }
    return res;
}
/**
 * 记录以arrY[index]到最后这个子数组中  不重复个数的累加
 * 如arrY=[1,1,5,5,4],index=0时返回--->[1,1,2,2,3]
 * 如arrY=[1,1,5,5,4],index=1时返回--->[1,2,2,3]
 * @param arrY
 * @param index
 * @return
 */
private static int[] CountOfdistinctsubArrY(int[] arrY,int index){
    int[] res=new int[arrY.length-index];
    int[] countNums = new int[51];
    for (int i = index; i <arrY.length ; i++) {
        int count=0;
        countNums[arrY[i]]++;
        for (int j = 0; j <countNums.length ; j++) {
            if(countNums[j]>=1){
                count++;
            }
        }
        res[i-index]=count;
    }
    return res;
}
}
'''

import sys
def getMax(arr1, arr2):
    n = len(arr1)
    res = -sys.maxsize
    for i in range(n):
        resA = getPreSum(arr1, i)
        resB = getDistinct(arr2, i)
        for i in range(n):
            res = max(res, resA[i] * resB[i])
    return res


def getPreSum(arr, index):
    n = len(arr)
    if n == 0:
        return 0
    res = [0 for _ in range(n)]
    res[index] = arr[index]
    for i in range(index + 1, n):
        res[i] = arr[i] + res[i - 1]
    return res


def getDistinct(arr, index):
    n = len(arr)
    if n == 0:
        return 0
    hash = [0 for _ in range(50)]
    res = [0 for i in range(n - index)]
    for i in range(index, n):
        cnt = 0
        hash[arr[i]] += 1
        for j in range(n):
            if hash[j] == 1:
                cnt += 1
        res[i - index] = cnt
    return res

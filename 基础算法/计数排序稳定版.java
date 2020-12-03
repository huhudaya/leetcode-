// 原始数列的规模是N，最大最小的差值是M，计数排序的时间复杂度和空间复杂度是多少？
// 第1，2，4都是遍历原始数组，时间复杂度都是N，第3步是遍历统计数组，运算量是M

// 把握住重点
// array[i]-min是countArray数组的下标
// 变形之前countArray[array[i]-min] 表示array[i]的个数
// 变形之后countArray[array[i]-min] 表示array[i]的排名

// 稳定版本 稳定是指保证原有的顺序不变
package com.study.spark.project.util;
import java.util.Arrays;
/**
 *
 * @description:
 * @author: Kai_Hu
 * @create: 2019-05-05 11:02
 **/
public class TestSortedArray {
    public static int[] countSort(int[] array) {
//1.得到数列的最大值和最小值，并算出差值d
        int max = array[0];
        int min = array[0];
        for(int i=1; i<array.length; i++) {
            if(array[i] > max) {
                max = array[i];
            }
            if(array[i] < min) {
                min = array[i];
            }
        }
        int d = max - min;
//2.创建统计数组并统计对应元素个数
        int[] countArray = new int[d+1]; //数组中的元素初始化为0
        for(int i=0; i<array.length; i++) {
            //将min作为基准数值
            countArray[array[i] - min]++;  //countArray的数组下标表示的是原始数组array中的元素伪排序到countArray中，countArray的数组下标对应count数组中的数据，countArray下标对应的元素值表示count数组中对应元素的个数，
        }
//不稳定版则可以直接输出
/*
        注意理解 array[i]是countArray的下标
        int index = 0;
        for(int i=0;i<=countArray.length;i++){
            for(int j=0;j<countArray[i];j++){ //这里的j表示countArray数组如果有数，则遍历。这里需要注意，如果countArray[]中的元素大于0，才会输出，如果等于0，此时j<countArray[]不成立
                sortedArray[index] = i+min;
                index++
            }
        }
*/
//构造前缀和数组
//3.统计数组做变形，后面的元素等于前面的元素之和。这样相加的目的，是让统计数组存储的元素值，等于相应整数的最终排序位置
        int sum = 0;
        for(int i = 0; i < countArray.length; i++) {
            sum += countArray[i];
            countArray[i] = sum;
        }
//4.倒序遍历原始数列，从统计数组找到正确位置，输出到结果数组 当前位置的值等于前一个位置元素的值加当前位置元素的值
        int[] sortedArray = new int[array.length];  //sortedArray数组的长度等于原始数组array的长度
        //对原始数组从后往前遍历
        for(int i = array.length - 1; i >= 0; i--) {
            //将countArray对应下标的数据的值减一，作为sortArray对应下标的值，countArray[array[i]-min]表示的是
            sortedArray[countArray[array[i] - min] - 1] = array[i];   //排名第1对应数组的第0个元素，所以需要减1
            countArray[array[i] - min]--;  //牢记countArray数组下标表示array中的元素
        }
        return sortedArray;
    }
    public static void main(String[] args) {
//        int[] array = new int[] {95,94,91,98,99,90,99,93,91,92};
        int[] array  = new int[] {90,99,95,94,95};
        int[] sortedArray = countSort(array);
        System.out.println(Arrays.toString(sortedArray));
    }
}


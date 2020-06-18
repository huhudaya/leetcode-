package com.study.spark.project.util;/**
 * @program: SparkTrain
 * @description: 桶排序
 * @author: Kai_Hu
 * @create: 2019-05-05 13:10
 * 注意桶排序的思路
 桶中最好是用插入排序进行排序，保证排序的稳定性

 **/

// 桶排序(Bucket Sort)，总结：
// 桶排序，是一种复杂度为O(n)的排序
// 桶排序，是一种稳定的排序
/*
桶排序需要两个辅助空间：
第一个辅助空间，是桶空间B
第二个辅助空间，是桶内的元素链表空间
总的来说，空间复杂度是O(n)。
桶排序有两个关键步骤：
扫描待排序数据A[N]，对于元素A[i]，放入对应的桶X
A[i]放入桶X，如果桶X已经有了若干元素，使用插入排序，将arr[i]放到桶内合适的位置
画外音：
（1）桶X内的所有元素，是一直有序的；
（2）插入排序是稳定的，因此桶内元素顺序也是稳定的；
当arr[N]中的所有元素，都按照上述步骤放入对应的桶后，就完成了全量的排序。
桶排序的伪代码是：
bucket_sort(A[N]){
     for i =1 to n{
           将A[i]放入对应的桶B[X];
           使用插入排序，将A[i]插入到B[X]中正确的位置;
     }
     将B[X]中的所有元素，按顺序合并，排序完毕;
}
桶排序，适用于数据均匀分布在一个区间内的场景
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
@SuppressWarnings("ALL")
public class BucketSort {
    public static double[] bucketSort(double[] array){
//1.得到数列的最大值和最小值，并算出差值d
        double max = array[0];
        double min = array[0];
        for(int i=1; i<array.length; i++) {
            if(array[i] > max) {
                max = array[i];
            }
            if(array[i] < min) {
                min = array[i];
            }
        }
        double d = max - min;
//2.初始化桶
        int bucketNum = array.length;
        //ArrayList里面是LinkedList数组，LinkedList里面是Double类型的数据
        ArrayList<LinkedList<Double>> bucketList = new ArrayList<LinkedList<Double>>(bucketNum);
        for(int i = 0; i < bucketNum; i++){
            bucketList.add(new LinkedList<Double>());
        }
//3.遍历原始数组，将每个元素放入桶中
        for(int i = 0; i < array.length; i++){
            //存到哪一个桶中，桶的序号是多少  这里 d= max-min,这里最后一个桶只存放最大值
            // 区间跨度 = (最大值-最小值）/ (桶的数量 - 1）   d=max-min
            int num = (int)((array[i] - min) * (bucketNum-1) / d);
            bucketList.get(num).add(array[i]);
        }
//4.对每个桶内部进行排序
        for(int i = 0; i < bucketList.size(); i++){
//JDK底层采用了归并排序或归并的优化版本 会将数组进行排序，这里最好使用插入排序进行排序，这样可以保正桶排序的稳定性
            Collections.sort(bucketList.get(i));
        }
//5.输出全部元素
        double[] sortedArray = new double[array.length];
        int index = 0;
        for(LinkedList<Double> list : bucketList){
            for(double element : list){
                sortedArray[index++] = element;
            }
        }
        return sortedArray;
    }
    public static void main(String[] args) {
        double[] array = new double[] {4.12,6.421,0.0023,3.0,2.123,8.122,4.12, 10.09};
        double[] sortedArray = bucketSort(array);
        System.out.println(Arrays.toString(sortedArray));
    }
}
'''
给定一个文件 file.txt，转置它的内容。

你可以假设每行列数相同，并且每个字段由 ' ' 分隔.

示例:

假设 file.txt 文件内容如下：

name age
alice 21
ryan 30
应当输出：

name alice ryan
age 21 30
'''
# 使用awk
'''
awk '{ #这个大括号里的代码是 对正文的处理
    # NF表示列数，NR表示已读的行数
    # 注意for中的i从1开始，i前没有类型
    for (i=1; i<=NF; i++){#对每一列
        if(NR==1){       #如果是第一行
            #将第i列的值存入res[i],$i表示第i列的值，i为数组的下标，以列序号为下标，
            #数组不用定义可以直接使用
            res[i]=$i;   
        }
        else{
            #不是第一行时，将该行对应i列的值拼接到res[i]
            res[i]=res[i] " " $i
        }
    }
}
# BEGIN{} 文件进行扫描前要执行的操作；END{} 文件扫描结束后要执行的操作。
END{
    #输出数组
	for (i=1; i<=NF; i++){
		print res[i]
	}
}' file.txt

'''
# python3
# python3 -c 'print("\n".join(map(" ".join,zip(*map(str.split,open("file.txt").readlines())))))'


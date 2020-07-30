'''
题干：
魔术师手中有一堆扑克牌， 但是被选中观众不知道它的顺序。
第一步， 魔术师从牌顶拿出一张牌， 放到桌子上。
第二步， 魔术师从牌顶再拿一张牌， 放在手上牌的底部。
第三步， 重复第一/二步的操作， 直到魔术师手中所有的牌都放到了桌子上。
然后观众根据桌子上扑克牌的顺序说出原来魔术师刚开始手上扑克牌的顺序。
示例：

输入：nums =  [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
输出：[1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10, 7]
题目分析：
此题不难，题目已经给出了得到桌面上扑克牌顺序的规则，我们只要逆推回去就可以，比如我们逆推一下案例，总结一下逆推的规则：我们现在拿13这张牌，在取出12这张牌，直接放到13上面即可，得到[12, 13]（为什么直接放？我们设想一下按照题目规则来说，剩下两张牌的时候，[12, 13]，12取出，13自己一张牌，放底部也是13啊），在取出11这张牌，规则反着来，取出13放顶部，再将11放顶部，得到[11, 13, 12]，在取出10这张牌，规则反着来，取出12放顶部，再将10放顶部，得到[10, 12, 11, 13]，以此类推......最后得到[1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10, 7]。
逆推的规则：
第一步，从手中的牌底拿出一张牌，放到手中牌的牌顶。
第二步，从桌子上牌顶拿出一张牌，放到手中牌的牌顶。
第三步， 重复第一/二步的操作， 直到桌子上所有的牌都放到了手中。
这样就得到了魔术师刚开始手上扑克牌的顺序
新手有可能遇到的解题思路陷阱：
自己根据想的案例总结规律，其实规律题目已经给出了，只需要反过来就可以。
解题思路分析以及代码实现：
第一种思路：逆推规则，利用队列的先进先出的特性，可以将先添加进入的元素取出在添加（模拟从牌尾到牌顶的过程） 。
第一种思路代码：

	private static int[] PlayingCardOrder(int[] numbers) {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(numbers[0]);
		queue.add(numbers[1]);
		for (int i = 2; i < numbers.length; i++) {
			queue.add(queue.poll());
			queue.add(numbers[i]);
		}
		//此时队列中的顺序是魔术师刚开始手上扑克牌的顺序的倒序
		int[] orderNumbers = new int[numbers.length];
		int i = numbers.length - 1;
		while (!queue.isEmpty()) {
			orderNumbers[i] = queue.poll();
			i--;
		}
		return orderNumbers;
	}
'''

'''
思路如下：由题意可知存在两种操作
1.摸牌；2.放牌；且两种操作交替进行，直到手牌为空。
因此可以将摸牌操作是为偶数，放牌操作视为奇数，设置一个标记量
当标记为偶数的时候摸牌，标记为奇数的时候放牌，从而有了大体的操作思路。
我们假设现在拿到的是最开始时候的有序牌堆，用每张牌的位置为牌编号
即为1-n号牌（在程序中用0~n-1实现），然后设置刚才提到的标记量从0开始，一直到数组长度-1，当标记量为偶数时，将对应标记取出放入一个新数组res中暂存
当标记量为奇数时将对应标记加到数组末尾，然后跳过该标记。
同时实时更新数组长度，直到所有的牌都被放入res中（即标记量=数组长度，意味着最后一张牌放入后数组中没有新牌，不再增加长度）。
此时res中牌的顺序就是题目给出的当前桌子上牌的顺序。
如果要还原，则将res与给出的桌子上牌的顺序Nums一一对应，创建一个长度为n的空result数组来存储数据，res中存的是nums中元素的原位置，设k为res的某个下标，则result【res[k]】的值就是nums[k]的值，按照这个思路将result还原出来即可得到原数组。

'''

# python实现（将原数组打乱）（用C + +也可以，把list改成vector即可，功能是类似的）：
def disorder():
    nums = [1, 3, 5, 4, 2]  # nums为顺序牌堆数组，输出的是排序后的数组
    list1 = []
    list2 = []
    n = len(nums)
    # list1记录的是数组的索引下标
    for i in range(0, n):
        list1.append(i)
    mark = 0
    lenth = len(list1)
    while mark < lenth:
        if mark % 2 == 0:
            list2.append(list1[mark])
        else:
            list1.append(list1[mark])
            lenth += 1
        mark += 1
    res = []
    for i in list2:
        res.append(nums[i])
    print(res)
print(disorder())

# python实现（将打乱数组还原，nums为展示在桌面上的数组，求原数组）
def convert():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    list1 = []
    list2 = []
    n = len(nums)
    for i in range(0, n):
        list1.append(i)
    mark = 0
    lenth = len(list1)
    while mark < lenth:
        if mark % 2 == 0:
            list2.append(list1[mark])
        else:
            list1.append(list1[mark])
            lenth += 1
        mark += 1
    res = [0 for _ in range(n)]
    for i in range(len(list2)):
        res[list2[i]] = nums[i]
    print(res)

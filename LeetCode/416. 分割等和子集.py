'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
'''
'''
这里可能会有人困惑为什么压缩到一维时，要采用逆序。
因为在一维情况下，是根据 dp[j] || dp[j - nums[i]]来推d[j]的值
如不逆序，就无法保证在外循环 i 值保持不变 j 值递增的情况下，dp[j - num[i]]的值不会被当前所放入的nums[i]所修改
当j值未到达临界条件前，会一直被nums[i]影响，也即是可能重复的放入了多次nums[i]，为了避免前面对后面产生影响
故用逆序。
 举个例子，数组为[2,2,3,5]，要找和为6的组合，i = 0时，dp[2]为真
 当i自增到1，j = 4时，nums[i] = 2,dp[4] = dp[4] || dp[4 - 2]为true，当i不变
 j = 6时,dp[6] = dp [6] || dp [6 - 2],而dp[4]为true，所以dp[6] = true,显然是错误的
 故必须得纠正在正序情况下，i值不变时多次放入nums[i]的情况
'''
# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485064&idx=1&sn=550705eb67f5e71487c8b218382919d6&chksm=9bd7f880aca071962a5a17d0f85d979d6f0c5a5ce32c84b8fee88e36d451f9ccb3bb47b88f78&scene=21#wechat_redirect
'''
第一步要明确两点，「状态」和「选择」。

    这个前文 经典动态规划：0-1 背包问题 已经详细解释过了，状态就是「背包的容量」和「可选择的物品」，选择就是「装进背包」或者「不装进背包」。
    
第二步要明确dp数组的定义。

    按照背包问题的套路，可以给出如下定义：

    dp[i][j] = x表示，对于前i个物品，当前背包的容量为j时，若x为true，则说明可以恰好将背包装满，若x为false，则说明不能恰好将背包装满。
    
    比如说，如果dp[4][9] = true，其含义为：对于容量为 9 的背包，若只是用前 4 个物品，可以有一种方法把背包恰好装满。
    
    或者说对于本题，含义是对于给定的集合中，若只对前 4 个数字进行选择，存在一个子集的和可以恰好凑出 9。
    
    根据这个定义，我们想求的最终答案就是dp[N][sum/2]，base case 就是dp[..][0] = true和dp[0][..] = false，因为背包没有空间的时候，就相当于装满了，而当没有物品可选择的时候，肯定没办法装满背包。

第三步，根据「选择」，思考状态转移的逻辑。

    回想刚才的dp数组含义，可以根据「选择」对dp[i][j]得到以下状态转移：
    
    如果不把nums[i]算入子集，或者说你不把这第i个物品装入背包，那么是否能够恰好装满背包，取决于上一个状态dp[i-1][j]，继承之前的结果。
    
    如果把nums[i]算入子集，或者说你把这第i个物品装入了背包，那么是否能够恰好装满背包，取决于状态dp[i - 1][j-nums[i-1]]。
    
    首先，由于i是从 1 开始的，而数组索引是从 0 开始的，所以第i个物品的重量应该是nums[i-1]，这一点不要搞混。
    
    dp[i - 1][j-nums[i-1]]也很好理解：你如果装了第i个物品，就要看背包的剩余重量j - nums[i-1]限制下是否能够被恰好装满。
    
    换句话说，如果j - nums[i-1]的重量可以被恰好装满，那么只要把第i个物品装进去，也可恰好装满j的重量；否则的话，重量j肯定是装不满的。
'''
'''
bool canPartition(vector<int>& nums) {
    int sum = 0;
    for (int num : nums) sum += num;
    // 和为奇数时，不可能划分成两个和相等的集合
    if (sum % 2 != 0) return false;
    int n = nums.size();
    sum = sum / 2;
    vector<vector<bool>> 
        dp(n + 1, vector<bool>(sum + 1, false));
    // base case
    for (int i = 0; i <= n; i++)
        dp[i][0] = true;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            if (j - nums[i - 1] < 0) {
               // 背包容量不足，不能装入第 i 个物品
                dp[i][j] = dp[i - 1][j]; 
            } else {
                // 装入或不装入背包
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j-nums[i-1]];
            }
        }
    }
    return dp[n][sum];
}
'''
'''
bool canPartition(vector<int>& nums) {
    int sum = 0, n = nums.size();
    for (int num : nums) sum += num;
    if (sum % 2 != 0) return false;
    sum = sum / 2;
    vector<bool> dp(sum + 1, false);
    // base case
    dp[0] = true;

    for (int i = 0; i < n; i++) 
        for (int j = sum; j >= 0; j--) 
            if (j - nums[i] >= 0) 
                dp[j] = dp[j] || dp[j - nums[i]];

    return dp[sum];
}
'''
from typing import List


# bitset方法
class Solution:
    def canPartition(self, nums):

        flag = 1  # 初始化
        sumnums = 0
        for i in nums:
            sumnums += i  # 记录和
            flag = flag | flag << i  # 记录所有可能的结果

        if sumnums % 2 == 0:  # 和为偶数才有解
            sumnums //= 2
        else:
            return False

        target = 1 << sumnums  # 目标和

        if target & flag != 0:  # 目标位置上不为0
            return True
        else:
            return False

    # hashset
    # 主要思想为：记录对nums取所有组合下可能出现的和，最后判断总和的一半是否在这些和中，其实还是动态规划
    # 以下实现进行了提前结束，迭代时的哈希判断等优化
    def canPartition(self, nums: List[int]) -> bool:
        target, remain = divmod(sum(nums), 2)
        if remain:  # 如果不能整除直接返回
            return False
        ans = {0}
        for i in nums:
            for j in list(ans):  # 循环中会改变ans
                j += i
                if j == target:  # 提前结束
                    return True
                ans.add(j)  # 之前的结果加当前数能得到的结果
        return False


# 如果正序遍历，这样只能是考虑到左上角和正上方的点，如果是正序，可能会重复
# 比如dp[2][4]会用到dp[0][3],但是只能用dp[1][3]，会出现覆盖更新，比如前面一层已经更新了dp[i]，本轮前面的j又更新了一次dp[i],这样dp[i]就被重新赋值了，实际上本轮循环只能看上一次循环的结果dp
# 如果是倒序的话，就不会出现这种情况
# 如果是倒序，则j-num[i]，这个时候j是递减的，此时j-num[i]的值也是递减的，这样就可以确保j只会使用到上一层循环得到的dp数组！如果进行更新dp数组，是不影响结果的，因为循环的时候只看左上角区域的值，倒着遍历的时候j减小的过程中，不会使用到本轮更新的dp数组


# 不压缩
# dp[i][j] = x表示，对于前i个物品，当前背包的容量为j时，若x为true，则说明可以恰好将背包装满，
# 若x为false，则说明不能恰好将背包装满。
'''
bool canPartition(vector<int>& nums) {
    int sum = 0;
    for (int num : nums) sum += num;
    // 和为奇数时，不可能划分成两个和相等的集合
    if (sum % 2 != 0) return false;
    int n = nums.size();
    sum = sum / 2;
    vector<vector<bool>> 
        dp(n + 1, vector<bool>(sum + 1, false));
    // base case
    for (int i = 0; i <= n; i++)
        dp[i][0] = true;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            if (j - nums[i - 1] < 0) {
               // 背包容量不足，不能装入第 i 个物品
                dp[i][j] = dp[i - 1][j]; 
            } else {
                // 装入或不装入背包,注意0/1背包和完全背包的区别，0/1背包问题中nums数组中的元素不可以重复利用！所以必须是dp[i-1]表示使用前N个物品
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j-nums[i-1]];
            }
        }
    }
    return dp[n][sum];
}
'''

# 压缩后
# dp[i][j] = x 表示，对于前i个物品
# 当前背包的容量为j时，若x为true，则说明可以恰好将背包装满，若x为false，则说明不能恰好将背包装满。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        n = len(nums)
        if _sum & 1:  # 是奇数
            return False
        target = _sum // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True  # dp[0][0]
        for i in range(n):
            for j in range(target, -1, -1):
                # 相当于剪枝
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]  # 保证本轮的dp值的更新不影响后面的结果
        return dp[target]


# 再次优化
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        n = len(nums)
        if _sum & 1: #是奇数
            return False
        target = _sum // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True #dp[0][0]
        for i in range(n):
            # 这里只需要判断到 i-1 即可
            for j in range(target, i - 1, -1):
                # 相当于剪枝
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]] # 保证本轮的dp值的更新不影响后面的结果
        return dp[target]
'''
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。
'''
import collections


# 利用树的序列化唯一来进行判断
class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []

        def collect(node):
            if not node:
                return "#"
            # 这里为前序遍历
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            # 这里为后序遍历
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        from collections import defaultdict
        res = []
        lookup = defaultdict(int)

        def helper(root):
            if not root:
                return "#"
            s = helper(root.left) + "," + helper(root.right) + "," + str(root.val)
            if lookup[s] == 1:
                res.append(root)
            lookup[s] += 1
            return s

        helper(root)
        return res


# java
'''
class Solution {
    int t;
    Map<String, Integer> trees;
    Map<Integer, Integer> count;
    List<TreeNode> ans;

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        t = 1;
        trees = new HashMap();
        count = new HashMap();
        ans = new ArrayList();
        lookup(root);
        return ans;
    }

    public int lookup(TreeNode node) {
        if (node == null) return 0;
        String serial = node.val + "," + lookup(node.left) + "," + lookup(node.right);
        int uid = trees.computeIfAbsent(serial, x-> t++);
        count.put(uid, count.getOrDefault(uid, 0) + 1);
        if (count.get(uid) == 2)
            ans.add(node);
        return uid;
    }
}
'''

'''
想法很简单，把数字符串化作为key放到map里，后续一旦出现相同的key说明出现了相同的树结构。
class Solution {
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        List<TreeNode> res = new ArrayList<TreeNode>();
        findDuplicateSubtrees(root, res, map);
        return res;
    }
    
    private StringBuilder findDuplicateSubtrees(TreeNode root, List<TreeNode> res, Map<String, Integer> map){
        if(root == null){
            return new StringBuilder("$");
        }
        StringBuilder left = findDuplicateSubtrees(root.left, res, map);
        StringBuilder right = findDuplicateSubtrees(root.right, res, map);
        //注意这里的加和顺序
        // StringBuilder treeKey = left.append(new StringBuilder(root.val + "")).append(right);
        StringBuilder treeKey = new StringBuilder(root.val + "").append(left).append(right);
        map.put(treeKey.toString(), map.getOrDefault(treeKey.toString(), 0) + 1);
        if(map.get(treeKey.toString()) == 2){
            res.add(root);
        }
        return treeKey;
    }
}
'''

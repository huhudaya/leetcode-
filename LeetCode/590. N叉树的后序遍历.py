'''
给定一个 N 叉树，返回其节点值的后序遍历。
例如，给定一个 3叉树 :

返回其后序遍历: [5,6,3,2,4,1].
说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''
'''
一 算法思路
1 递归
（1）递归边界处理：空树直接返回[]。
（2）对于非空的情况，首先递归调用函数本身顺序处理当前节点的各个子节点，并将访问到的各个节点值添加到结果列表中，最后再访问当前节点。之后返回结果列表。
2 栈（非递归）
正难则反
首先访问根节点，再将其子节点从左到右入栈，这样首先出栈的是它的最后一个子节点，因此得到的结果与要求是相反的，所以最后将列表反转输出即可。
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if root is None:
            return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res

    # method 2
    def postorder(self, root):
        if root is None:
            return []
        st = [root]
        res = []
        while st:
            p = st.pop()
            res.append(p.val)
            for child in p.children:
                st.append(child)
        return res[::-1]


'''
class Solution {
    public List<Integer> postorder(Node root) {
        LinkedList<Node> stack = new LinkedList<>();
        LinkedList<Integer> output = new LinkedList<>();
        if (root == null) {
            return output;
        }

      stack.add(root);
      while (!stack.isEmpty()) {
          Node node = stack.pollLast();
          output.addFirst(node.val);
          for (Node item : node.children) {
              if (item != null) {
                  stack.add(item);    
              } 
          }
      }
      return output;
    }
}
'''

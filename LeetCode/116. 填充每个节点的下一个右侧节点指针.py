'''
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

示例：
输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

提示：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
'''

# 递归
def connect(self, root: 'Node') -> 'Node':
    if not root:
        return
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
    self.connect(root.left)
    self.connect(root.right)
    return root

# 迭代 相当于是层次遍历
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pre = root
        # pre相当于当前层的第一个节点
        while pre:
            cur = pre
            # 相当于层次遍历 cur为当前层中的节点
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root

# GO 迭代
'''
func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	n := root
    var nextLevel *Node
	for n.Left != nil {       // 一直循环到纯叶子节点为止
		nextLevel = n.Left   // 保留下一层的最左侧第一个叶子节点
		for n != nil {          // 迭代本层的每个节点
			n.Left.Next = n.Right  // 把这个节点的左侧子节点的next指向右侧子节点
			if n.Next != nil {     // 当这个节点的next节点不是空的时候
				n.Right.Next = n.Next.Left  // 把这个节点的右侧子节点的next指向这个节点的Next节点的左侧子节点
			}
			n = n.Next          // 迭代本层的下一个节点
		}
		n = nextLevel         // 本层迭代完了，让我们开始迭代下一层 
	}
	return root
}
'''
# go dfs
'''
func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	l := root.Left
	r := root.Right
	for l != nil {
		l.Next = r //连接
		l = l.Right //往右
		r = r.Left //往左
	}
	connect(root.Left)
	connect(root.Right)
	return root
}
'''

# java
'''
class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        if (root.left != null) {
            root.left.next = root.right;
            if (root.next != null) root.right.next = root.next.left;
        }
        connect(root.left);
        connect(root.right);
        return root;
    }
}

# 迭代
class Solution {
    public Node connect(Node root) {
        Node pre = root;
        while (pre != null) {
            Node cur = pre;
            while (cur != null) {
                if (cur.left != null) cur.left.next = cur.right;
                if (cur.right != null && cur.next != null) cur.right.next = cur.next.left;
                cur = cur.next;
            }
            pre = pre.left;
        }
        return root;
    }
}
'''

# java
'''
每个 node 左子树的 next , 就是 node 的右子树
每个 node 右子树的 next, 就是 node next 的 左子树

public Node connect(Node root) {
    dfs(root, null);
    return root;
}

private void dfs(Node node, Node next) {
    if(node != null) {
        node.next = next;
        dfs(node.left, node.right);
        dfs(node.right, node.next != null ? node.next.left : null);
    }
}
'''
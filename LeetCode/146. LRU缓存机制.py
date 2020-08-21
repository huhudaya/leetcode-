'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

 

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
'''
'''
import java.util.HashMap;
import java.util.Map;

public class LRUCache {

    private Map<Integer, ListNode> map;

    /**
     * 双链表结点类
     */
    private class ListNode {

        private Integer key;
        private Integer value;
        /**
         * 前驱结点 precursor
         */
        private ListNode pre;
        /**
         * 后继结点 successor（写成 next 是照顾单链表的表示习惯）
         */
        private ListNode next;

        public ListNode() {
        }

        public ListNode(Integer key, Integer value) {
            this.key = key;
            this.value = value;
        }
    }

    private int capacity;

    /**
     * 虚拟头结点没有前驱
     */
    private ListNode dummyHead;
    /**
     * 虚拟尾结点没有后继
     */
    private ListNode dummyTail;

    public LRUCache(int capacity) {
        map = new HashMap<>(capacity);
        this.capacity = capacity;
        dummyHead = new ListNode(-1, -1);
        dummyTail = new ListNode(-1, -1);
        // 初始化链表为 head <-> tail

        dummyHead.next = dummyTail;
        dummyTail.pre = dummyHead;
    }

    /**
     * 如果存在，把当前结点移动到双向链表的头部
     *
     * @param key
     * @return
     */
    public int get(int key) {
        if (map.containsKey(key)) {
            //hash中的key指向的value是一个链表中的节点
            ListNode node = map.get(key);
            int val = node.value;

            // 把当前 node 移动到双向链表的头部
            moveNode2Head(key);
            return val;
        } else {
            return -1;
        }
    }

    /**
     * 如果哈希表的容量满了，就要删除一个链表末尾元素，然后在链表头部插入新元素
     *
     * @param key
     * @param value
     */
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            // 1、更新 value
            map.get(key).value = value;
            // 2、把当前 node 移动到双向链表的头部
            moveNode2Head(key);
            return;
        }

        // 放元素的操作是一样的

        if (map.size() == capacity) {
            // 如果满了
            ListNode oldTail = removeTail();

            // 设计 key 就是为了在这里删除
            map.remove(oldTail.key);
        }

        // 然后添加元素
        ListNode newNode = new ListNode(key, value);
        map.put(key, newNode);
        addNode2Head(newNode);
    }

    // 为了突出主干逻辑，下面是 3 个公用的方法

    /**
     * 删除双链表尾部结点
     */
    private ListNode removeTail() {
        ListNode oldTail = dummyTail.pre;
        ListNode newTail = oldTail.pre;

        // 两侧结点建立连接
        newTail.next = dummyTail;
        dummyTail.pre = newTail;

        // 释放引用
        oldTail.pre = null;
        oldTail.next = null;

        return oldTail;
    }

    /**
     * 把当前 key 指向的结点移到双向链表的头部
     *
     * @param key
     */
    private void moveNode2Head(int key) {
        // 1、先把 node 拿出来
        ListNode node = map.get(key);

        // 2、原来 node 的前驱和后继接上
        node.pre.next = node.next;
        node.next.pre = node.pre;

        // 3、再把 node 放在末尾
        addNode2Head(node);
    }

    /**
     * 在双链表的头部新增一个结点
     *
     * @param newNode
     */
    private void addNode2Head(ListNode newNode) {
        // 1、当前头结点
        ListNode oldHead = dummyHead.next;

        // 2、末尾结点的后继指向新结点
        oldHead.pre = newNode;

        // 3、设置新结点的前驱和后继
        newNode.pre = dummyHead;
        newNode.next = oldHead;

        // 4、更改虚拟头结点的后继结点
        dummyHead.next = newNode;
    }


    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.map.keySet());

        int res1 = cache.get(1);
        System.out.println(res1);

        cache.put(3, 3);

        int res2 = cache.get(2);
        System.out.println(res2);

        int res3 = cache.get(3);
        System.out.println(res3);

        cache.put(4, 4);
        System.out.println(cache.map.keySet());

        int res4 = cache.get(1);
        System.out.println(res4);

        int res5 = cache.get(3);
        System.out.println(res5);

        int res6 = cache.get(4);
        System.out.println(res6);
    }
}
'''

# java

'''
class LRUCache extends LinkedHashMap<Integer, Integer>{
    private int capacity;

    public LRUCache(int capacity) {
        super(capacity, 0.75F, true);
        this.capacity = capacity;
    }

    public int get(int key) {
        return super.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        super.put(key, value);
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
        return size() > capacity; 
    }
}
'''

# java
'''
class Node {
    public int key, val;
    public Node next, prev;
    public Node(int k, int v) {
        this.key = k;
        this.val = v;
    }
}

class DoubleList {  
    // 头尾虚节点
    private Node head, tail;  
    // 链表元素数
    private int size;

    public DoubleList() {
        // 初始化双向链表的数据
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    public void addFirst(Node x) {
        x.next = head.next;
        x.prev = head;
        head.next.prev = x;
        head.next = x;
        size++;
    }

    public void remove(Node x) {
        x.prev.next = x.next;
        x.next.prev = x.prev;
        size--;
    }

    public Node removeLast() {
        if (tail.prev == head)
            return null;
        Node last = tail.prev;
        remove(last);
        return last;
    }

    public int size() { return size; }
}

class LRUCache {

    private int cap;
    private HashMap<Integer, Node> map;
    private DoubleList cache;

    public LRUCache(int capacity) {
        // 初始化 LRU cache 的数据
        this.cap = capacity;
        map = new HashMap<>();
        cache = new DoubleList();
    }

    public int get(int key) {
        if (!map.containsKey(key))
            return -1;
        int val = map.get(key).val;
        put(key, val);
        return val;
    }

    public void put(int key, int val) {
        // 先把新节点 x 做出来
        Node x = new Node(key, val);

        if (map.containsKey(key)) {
            // 删除旧的，新的插到头部
            cache.remove(map.get(key));
            cache.addFirst(x);
            // 更新 map 中对应的数据
            map.put(key, x);
        } else {
            if (cap == cache.size()) {
                // 删除链表最后一个
                Node last = cache.removeLast();
                // 这一步很关键，一定要移除map中对应的key
                map.remove(last.key);
            }
            // 直接添加到头部即可
            cache.addFirst(x);
            map.put(key, x);
        }
    }
}
'''

# 核心思路
# 在双向链表的实现中，使用一个伪头部（dummy head）和伪尾部（dummy tail）标记界限
# 这样在添加节点和删除节点的时候就不需要检查相邻的节点是否存在

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


# 自己的版本
'''
为什么要在链表中同时存储 key 和 val，而不是只存储 val?
当缓存容量已满，我们不仅仅要删除最后一个 Node 节点
还要把 map 中映射到该节点的 key 同时删除
而这个 key 只能由 Node 得到。如果 Node 结构中只存储 val
那么我们就无法得知 key 是什么，就无法删除 map 中的键，造成错误。
'''


class DNode:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity: int):
        # 创建虚拟节点
        self.head = DNode()
        self.tail = DNode()
        # 缓存容量
        self.capacity = capacity
        # 当前大小
        self.size = 0
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 因为最近访问了，所以移到头节点
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DNode(key, value)
            # 添加到缓存哈希
            self.cache[key] = node
            self.addTohead(node)
            self.size += 1
            # 如果超出容量，删除尾部节点，同时将对应的缓存中的数据删除
            if self.size > self.capacity:
                tail_node = self.removeTail()
                self.cache.pop(tail_node.key)
                self.size -= 1
        # 如果在缓存中，将节点移到头节点
        else:
            # 此时node为链表中的元素，需要移到头节点
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addTohead(self, node):
        self.head.next.pre = node
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node):
        self.removeNode(node)
        self.addTohead(node)

    # 返回node是为了删除对应cache中的key
    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
import collections


class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)





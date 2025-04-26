# Assignment #9: Huffman, BST & Heap

Updated 1834 GMT+8 Apr 15, 2025

2025 spring, Complied by <mark>肖行宇 物院</mark>



> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### LC222.完全二叉树的节点个数

dfs, https://leetcode.cn/problems/count-complete-tree-nodes/

思路：



代码：

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-16%20183244.png)



### LC103.二叉树的锯齿形层序遍历

bfs, https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

思路：



代码：

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]

        def dfs(stack=[root], i=0):
            nex = []
            if i % 2 == 0:
                while stack:
                    node = stack.pop()
                    if node is not None:
                        if node.right is not None:
                            nex.append(node.right)
                        if node.left is not None:
                            nex.append(node.left)
                if not nex:
                    return
                val_nex = [node.val for node in nex]
                ans.append(val_nex)
            else:
                while stack:
                    node = stack.pop()
                    if node is not None:
                        if node.left is not None:
                            nex.append(node.left)
                        if node.right is not None:
                            nex.append(node.right)
                if not nex:
                    return
                val_nex = [node.val for node in nex]
                ans.append(val_nex)

            dfs(nex, i+1)
        
        dfs()
        return ans
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-16%20192529.png)



### M04080:Huffman编码树

greedy, http://cs101.openjudge.cn/practice/04080/

思路：



代码：

```python
import heapq
n = int(input())
s = list(map(int, input().split()))
heapq.heapify(s)
ans = 0
while len(s) > 1:
    a = heapq.heappop(s)
    b = heapq.heappop(s)
    heapq.heappush(s, a+b)
    ans += (a+b)
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-22%20181410.png)



### M05455: 二叉搜索树的层次遍历

http://cs101.openjudge.cn/practice/05455/

思路：



代码：

```python
from collections import deque
s = list(map(int, input().split()))


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)
    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


a = {s[0]}
root = Node(s[0])
for x in s[1:]:
    if x in a:
        continue
    insert(root, x)
    a.add(x)
ans = [s[0]]


def dfs(stack=[root]):
    stack = deque(stack)
    nex = []
    while stack:
        node = stack.popleft()
        if node is not None:
            if node.left is not None:
                nex.append(node.left)
            if node.right is not None:
                nex.append(node.right)
    if not nex:
        return
    val_nex = [node.val for node in nex]
    ans.extend(val_nex)
    dfs(nex)


dfs()
print(*ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-22%20204635.png)



### M04078: 实现堆结构

手搓实现，http://cs101.openjudge.cn/practice/04078/

类似的题目是 晴问9.7: 向下调整构建大顶堆，https://sunnywhy.com/sfbj/9/7

思路：



代码：

```python
class Binaryheap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2
            if self.heap[i] < self.heap[parent_idx]:
                self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
                i = parent_idx
            else:
                break

    def pop(self):
        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]
        res = heap.pop()
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left
            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        return res


n = int(input())
heapq = Binaryheap()
for _ in range(n):
    s = input().split()
    if s[0] == '2':
        print(heapq.pop())
    else:
        heapq.push(int(s[1]))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-22%20224259.png)



### T22161: 哈夫曼编码树

greedy, http://cs101.openjudge.cn/practice/22161/

思路：



代码：

```python
import heapq


class Node:
    def __init__(self, weight, char=None):
        self.char = char
        self.weight = weight
        self.left = None
        self.right = None

    def __lt__(self, other):
        return (self.weight, self.char) < (other.weight, other.char)


def build_tree(characters):
    heap = []
    for char, weight in characters:
        heapq.heappush(heap, Node(weight, char))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.weight + right.weight)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]


def encode(root):
    codes = {}

    def traverse(node, code=''):
        if not node.left and not node.right:
            codes[node.char] = code
            return
        traverse(node.left, code+'0')
        traverse(node.right, code+'1')

    traverse(root)
    return codes


def add_code(string, codes):
    addcode = ''
    for c in string:
        addcode += codes[c]
    return addcode


def decode(root, code):
    string = ''
    node = root
    for bit in code:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            string += node.char
            node = root
    return string


n = int(input())
characters = []
for _ in range(n):
    char, weight = input().split()
    characters.append((char, int(weight)))
root = build_tree(characters)
codes = encode(root)

while True:
    try:
        s = input()
        if s[0] in ('1', '0'):
            print(decode(root, s))
        else:
            print(add_code(s, codes))
    except EOFError:
        break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-22%20233259.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

主要是了解了霍夫曼编码和二叉堆










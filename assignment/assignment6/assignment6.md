# Assignment #6: 回溯、树、双向链表和哈希表

Updated 1526 GMT+8 Mar 22, 2025

2025 spring, Complied by <mark>肖行宇  物院</mark>



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

### LC46.全排列

backtracking, https://leetcode.cn/problems/permutations/

思路：



代码：

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        p = [True]*n
        ans = []

        def dfs(lis=[], idx=0):
            if idx == n:
                ans.append(lis)
            for i in range(n):
                if p[i]:
                    p[i] = False
                    dfs(lis+[nums[i]], idx+1)
                    p[i] = True

        dfs()
        return ans
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-25%20175058.png)



### LC79: 单词搜索

backtracking, https://leetcode.cn/problems/word-search/

思路：



代码：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = []
        n, m = len(board), len(board[0])
        k = len(word)
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    starts.append((i, j))
        ans = False
        dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(start, idx=0):
            nonlocal ans
            if idx == k-1:
                ans = True
                return
            x, y = start
            for dx, dy in dire:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited.get((nx, ny), 0):
                    if board[nx][ny] == word[idx+1]:
                        visited[(nx, ny)] = 1
                        dfs((nx, ny), idx+1)
                        visited[(nx, ny)] = 0

        for start in starts:
            visited = {}
            visited[start] = 1
            dfs(start)
        return ans

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-25%20181214.png)



### LC94.二叉树的中序遍历

dfs, https://leetcode.cn/problems/binary-tree-inorder-traversal/

思路：



代码：

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(True, root)]
        ans = []
        while stack:
            judge, node = stack.pop()
            if node is None:
                continue
            if judge:
                stack.append((True, node.right))
                stack.append((False, node))
                stack.append((True, node.left))
            else:
                ans.append(node.val)
        return ans
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-26%20164304.png)



### LC102.二叉树的层序遍历

bfs, https://leetcode.cn/problems/binary-tree-level-order-traversal/

思路：



代码：

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]

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
            ans.append(val_nex)
            dfs(nex)

        dfs()
        return ans
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-26%20165814.png)



### LC131.分割回文串

dp, backtracking, https://leetcode.cn/problems/palindrome-partitioning/

思路：



代码：

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i+1, n+1):
                t = s[i:j]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j)
                    path.pop()

        dfs(0)
        return ans

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-26%20191122.png)



### LC146.LRU缓存

hash table, doubly-linked list, https://leetcode.cn/problems/lru-cache/

思路：



代码：

```python
class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.nex = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.tail = Node()
        self.head = Node()
        self.head.nex, self.tail.pre = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        node.pre.nex, node.nex.pre = node.nex, node.pre
        tail_pre = self.tail.pre
        tail_pre.nex, self.tail.pre, node.pre, node.nex = node, node, tail_pre, self.tail
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.pre.nex, node.nex.pre = node.nex, node.pre
        node = Node(key, value)
        tail_pre = self.tail.pre
        tail_pre.nex, self.tail.pre, node.pre, node.nex = node, node, tail_pre, self.tail
        self.key_to_node[key] = node
        if len(self.key_to_node) > self.capacity:
            last_node = self.head.nex
            del self.key_to_node[last_node.key]
            self.head.nex, last_node.nex.pre = last_node.nex, self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-27%20123157.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

对树有了一定了解。LRU缓存开始想用字典写，但是超时了，双向列表很巧妙。










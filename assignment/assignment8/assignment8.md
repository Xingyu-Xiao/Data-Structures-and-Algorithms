# Assignment #8: 树为主

Updated 1704 GMT+8 Apr 8, 2025

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

### LC108.将有序数组转换为二叉树

dfs, https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

思路：



代码：

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m = len(nums)//2
        return TreeNode(nums[m], self.sortedArrayToBST(nums[:m]), self.sortedArrayToBST(nums[m+1:]))
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-13%20223244.png)



### M27928:遍历树

 adjacency list, dfs, http://cs101.openjudge.cn/practice/27928/

思路：



代码：

```python
class TreeNode:
    def __init__(self, val):
        self.children = []
        self.par = None
        self.val = val


Node_dic = {}
n = int(input())
for _ in range(n):
    nodes = list(map(int, input().split()))
    if nodes[0] not in Node_dic:
        one = TreeNode(nodes[0])
        Node_dic[nodes[0]] = one
    else:
        one = Node_dic[nodes[0]]
    for node in nodes[1:]:
        if node not in Node_dic:
            nod = TreeNode(node)
            Node_dic[node] = nod
        else:
            nod = Node_dic[node]
        one.children.append(nod)
        nod.par = one

for node in Node_dic.values():
    if node.par is None:
        root = node

stack = [(True, root)]
ans = []
while stack:
    judge, node = stack.pop()
    if node is None:
        continue
    if judge:
        lis = node.children + [node]
        lis.sort(key=lambda x: x.val)
        for x in lis:
            if x == node:
                stack.append((False, x))
            else:
                stack.append((True, x))
    else:
        ans.append(node.val)
while ans:
    print(ans.pop())

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-13%20214903.png)



### LC129.求根节点到叶节点数字之和

dfs, https://leetcode.cn/problems/sum-root-to-leaf-numbers/

思路：



代码：

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        def dfs(node, s):
            if node.left is None and node.right is None:
                ans.append(int(s))
                return
            if node.left is not None:
                dfs(node.left, s+str(node.left.val))
            if node.right is not None:
                dfs(node.right, s+str(node.right.val))

        dfs(root, str(root.val))
        return sum(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-13%20221130.png)



### M22158:根据二叉树前中序序列建树

tree, http://cs101.openjudge.cn/practice/22158/

思路：



代码：

```python
def solve(pre, ino):
    if not pre:
        return ''
    root = pre[0]
    idx = ino.index(root)
    left_ino = ino[:idx]
    right_ino = ino[idx+1:]
    left_pre = pre[1:idx+1]
    right_pre = pre[idx+1:]
    return solve(left_pre, left_ino) + solve(right_pre, right_ino) + root


while True:
    try:
        pre = input()
        ino = input()
        print(solve(pre, ino))
    except EOFError:
        break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-14%20101038.png)



### M24729:括号嵌套树

dfs, stack, http://cs101.openjudge.cn/practice/24729/

思路：



代码：

```python
tree = input()
pre = tree.replace('(', '').replace(')', '').replace(',', '')
stack = []
beh = []
for char in tree:
    if char.isalpha():
        stack.append(char)
    if char == ')' or char == ',':
        beh.append(stack.pop())
beh.append(stack.pop())
print(pre)
print(''.join(beh))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-14%20103202.png)



### LC3510.移除最小数对使数组有序II

doubly-linked list + heap, https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/

思路：



代码：

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        class Node:
            def __init__(self, left, right, idx):
                self.pre = None
                self.left = left
                self.right = right
                self.idx = idx
                self.next = None

        n = len(nums)
        if n <= 1:
            return 0
        head = Node(nums[0], nums[1], 0)
        pr = head
        node_dic = {0: head}
        dec = 0 if nums[0] <= nums[1] else 1
        h = [(nums[0]+nums[1], 0)]
        for i in range(1, n-1):
            nxt = Node(nums[i], nums[i+1], i)
            node_dic[i] = nxt
            pr.next = nxt
            nxt.pre = pr
            pr = nxt

            x, y = nums[i], nums[i+1]
            h.append((x+y, i))
            if x > y:
                dec += 1
        heapq.heapify(h)

        ans = 0
        judge = [False]*(n-1)
        while dec:
            ans += 1
            new_val, idx = heapq.heappop(h)
            node = node_dic[idx]
            while node.right + node.left != new_val or judge[idx]:
                new_val, idx = heapq.heappop(h)
                node = node_dic[idx]
            judge[idx] = True
            if node.left > node.right:
                dec -= 1
            next_node = node.next
            pre_node = node.pre
            if next_node:
                if new_val > next_node.right:
                    dec += 1
                if next_node.left > next_node.right:
                    dec -= 1
                next_node.left = new_val
                next_node.pre = pre_node
                nxt_val = next_node.left + next_node.right
                nex_idx = next_node.idx
                heapq.heappush(h, (nxt_val, nex_idx))

            if pre_node:
                if pre_node.left > pre_node.right:
                    dec -= 1
                if new_val < pre_node.left:
                    dec += 1
                pre_node.right = new_val
                pre_node.next = next_node
                pre_val = pre_node.right + pre_node.left
                pre_idx = pre_node.idx
                heapq.heappush(h, (pre_val, pre_idx))

        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-15%20183919.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

最后一题难度比较大，花了很多时间，在进行懒删除时有些点很容易忽略。









7

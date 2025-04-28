# Assignment #A: Graph starts

Updated 1830 GMT+8 Apr 22, 2025

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

### M19943:图的拉普拉斯矩阵

OOP, implementation, http://cs101.openjudge.cn/practice/19943/

要求创建Graph, Vertex两个类，建图实现。

思路：



代码：

```python
n, m = map(int, input().split())
A = [[0]*n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    A[a][a] += 1
    A[b][b] += 1
    A[a][b] -= 1
    A[b][a] -= 1
for x in A:
    print(*x)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-26%20215035.png)



### LC78.子集

backtracking, https://leetcode.cn/problems/subsets/

思路：



代码：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        p = [True] * len(nums)

        def backtrack(n, res=[], i=0):
            if i == n:
                res.sort()
                ans.add(tuple(res))
                return
            for j in range(len(nums)):
                if p[j]:
                    p[j] = False
                    backtrack(n, res + [nums[j]], i + 1)
                    p[j] = True

        for k in range(len(nums)):
            backtrack(k)

        ans = list(set(ans))
        for i in range(len(ans)):
            ans[i] = list(ans[i])
        ans.append(nums)
        return ans

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-26%20231334.png)



### LC17.电话号码的字母组合

hash table, backtracking, https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

思路：



代码：

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = ['']*n
        def dfs(i=0):
            if i == n:
                ans.append(''.join(path))
                return
            for c in mapping[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs()
        return ans


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-28%20095222.png)



### M04089:电话号码

trie, http://cs101.openjudge.cn/practice/04089/

思路：



代码：

```python
n = int(input())
for _ in range(n):
    m = int(input())
    phonenumbers = [input() for _ in range(m)]
    phonenumbers.sort()
    for i in range(len(phonenumbers)-1):
        if phonenumbers[i] == phonenumbers[i+1][:len(phonenumbers[i])]:
            print('NO')
            break
    else:
        print('YES')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-28%20100404.png)



### T28046:词梯

bfs, http://cs101.openjudge.cn/practice/28046/

思路：



代码：

```python
from collections import deque, defaultdict
n = int(input())
words = [input() for _ in range(n)]
start, end = input().split()
word_set = set(words)
visited = {start:None}
queue = deque([start])
wildcard_map = defaultdict(list)
for word in word_set:
    for i in range(4):
        wildcard = word[:i] + '*' + word[i + 1:]
        wildcard_map[wildcard].append(word)
near = defaultdict(list)
for word in word_set:
    for i in range(4):
        wildcard = word[:i] + '*' + word[i + 1:]
        for neighbor in wildcard_map[wildcard]:
            if neighbor != word:
                near[word].append(neighbor)

def bfs():
    while queue:
        node = queue.popleft()
        for neighbor in near[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                if neighbor == end: return True
                queue.append(neighbor)


judge = bfs()
if judge:
    path = []
    node = end
    while node:
        path.append(node)
        node = visited[node]
    path.reverse()
    print(*path)
else:
    print('NO')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-28%20185959.png)



### T51.N皇后

backtracking, https://leetcode.cn/problems/n-queens/

思路：



代码：

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen = ['.']*n
        ans = []
        judge = [True]*n
        diag1 = [True]*(2*n-1)
        diag2 = [True]*(2*n-1)
        def dfs(lis=[],j=0):
            if j == n:
                ans.append(lis)
                return
            for i in range(n):
                if judge[i] and diag1[i+j] and diag2[i-j+n-1]:
                    judge[i] = False
                    diag1[i+j] = False
                    diag2[i-j+n-1] = False
                    dfs(lis+[i],j+1)
                    judge[i] = True
                    diag1[i+j] = True
                    diag2[i-j+n-1] = True
        dfs()
        for i in range(len(ans)):
            x = []
            for j in range(n):
                y = queen.copy()
                y[ans[i][j]] = 'Q'
                x.append(''.join(y))
            ans[i] = x
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-28%20202053.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次主要是dfs和bfs，上个学期练了很多所以写起来比较轻松










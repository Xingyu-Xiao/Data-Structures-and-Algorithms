# Assignment #7: 20250402 Mock Exam

Updated 1624 GMT+8 Apr 2, 2025

2025 spring, Complied by <mark>肖行宇  物院</mark>



> **说明：**
>
> 1. **⽉考**：AC?<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E05344:最后的最后

http://cs101.openjudge.cn/practice/05344/



思路：



代码：

```python
from collections import deque


def f(name_list, num):
    ans = []
    queue = deque(name_list)

    while len(queue) > 0:
        for i in range(num):
            queue.append(queue.popleft())
        ans.append(queue.popleft())
    ans.pop()
    return ans


n, m = map(int, input().split())
s = [i for i in range(1, n+1)]
print(' '.join(map(str, f(s, m-1))))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-02%20190940.png)

### M02774: 木材加工

binary search, http://cs101.openjudge.cn/practice/02774/



思路：



代码：

```python
n, k = map(int, input().split())
log = [int(input()) for _ in range(n)]


def num(logs, length):
    number = 0
    for x in logs:
        number += (x // length)
    return number


left, right = 0, max(log)
while left < right - 1:
    mid = (left + right) // 2
    number = num(log, mid)
    if number >= k:
        left = mid
    else:
        right = mid
print(left)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-03%20104309.png)



### M07161:森林的带度数层次序列存储

tree, http://cs101.openjudge.cn/practice/07161/



思路：



代码：

```python
class Tree:
    def __init__(self, name):
        self.children = []
        self.name = name


def printTree(root):
    stack = [(True, root)]
    ans = []
    while stack:
        judge, node = stack.pop()
        if node is None:
            continue
        if judge:
            stack.append((False, node))
            for child in node.children[::-1]:
                stack.append((True, child))
        else:
            ans.append(node.name)
    return ans


n = int(input())
out = []
for _ in range(n):
    inp = input().split()
    nu = [inp[i] for i in range(len(inp)) if i % 2 == 1]
    nodes = [Tree(x) for x in inp if x not in nu]
    num = list(map(int, nu))
    idx = num[0]
    root = nodes[0]
    root.children.extend(nodes[1:num[0]+1])
    for i in range(1, len(nu)):
        node = nodes[i]
        node.children.extend(nodes[idx+1:idx+1+num[i]])
        idx += num[i]
    out.extend(printTree(root))
print(*out)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-03%20113516.png)



### M18156:寻找离目标数最近的两数之和

two pointers, http://cs101.openjudge.cn/practice/18156/



思路：



代码：

```python
t = int(input())
s = list(map(int, input().split()))
s.sort()
i, j = 0, len(s)-1
if t >= s[-1] + s[-2]:
    ans = s[-1] + s[-2]
elif t <= s[0] + s[1]:
    ans = s[0] + s[1]
else:
    res = []
    while i < j:
        tar = s[i]+s[j]
        if tar > t:
            j -= 1
        else:
            i += 1
        res.append((abs(t-tar), tar))
    res.sort()
    ans = res[0][1]
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-03%20120223.png)



### M18159:个位为 1 的质数个数

sieve, http://cs101.openjudge.cn/practice/18159/



思路：



代码：

```python
t = int(input())
ns = [int(input()) for _ in range(t)]
n = max(ns)
s = [True]*(n+1)
num = []
for i in range(2,n+1):
    if s[i]:
        num.append(i)
    for j in range(i, n//i+1):
        s[j*i] = False
for i in range(t):
    ans = []
    for x in num:
        if str(x)[-1] == '1' and x < ns[i]:
            ans.append(x)
    print(f'Case{i+1}:')
    if ans:
        print(*ans)
    else:
        print('NULL')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-03%20133437.png)



### M28127:北大夺冠

hash table, http://cs101.openjudge.cn/practice/28127/



思路：



代码：

```python
m = int(input())
pass_num = {}
sub_num = {}
for i in range(m):
    team, problem, score = input().split(',')
    if score == 'yes':
        if team in pass_num:
            pass_num[team].add(problem)
        else:
            pass_num[team] = {problem}
    sub_num[team] = sub_num.get(team, 0) + 1
s = [(team, len(pass_num.get(team, [])), sub_num[team]) for team in sub_num]
s.sort(key=lambda x: (-x[1], x[2], x[0]))
for i, (team, pass_n, sub_n) in enumerate(s):
    if i == 12:
        break
    print(f'{i+1} {team} {pass_n} {sub_n}')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-04-03%20142758.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次月考忘记了结果没去，感觉还算比较简单，都自己ac了。










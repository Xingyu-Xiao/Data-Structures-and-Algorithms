# Assignment #3: 惊蛰 Mock Exam

Updated 1641 GMT+8 Mar 5, 2025

2025 spring, Complied by <mark>肖行宇 物院</mark>



> **说明：**
>
> 1. **惊蛰⽉考**：AC6<mark>（3）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
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

### E04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015



思路：



代码：

```python
def check(a):
    num = a.count('@')
    if num != 1:
        return 'NO'
    if a[0] == '@' or a[0] == '.':
        return 'NO'
    if a[-1] == '@' or a[-1] == '.':
        return 'NO'
    idx = a.index('@')
    if a[idx-1] == '.' or a[idx+1] == '.':
        return 'NO'
    if '.' not in a[idx+2:]:
        return 'NO'
    return 'YES'


while True:
    try:
        s = input()
        print(check(s))
    except EOFError:
        break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-07%20150052.png)



### M02039: 反反复复

implementation, http://cs101.openjudge.cn/practice/02039/



思路：



代码：

```python
n = int(input())
s = input()
m = len(s)//n
matrix = [['' for _ in range(n)] for _ in range(m)]
i = 0
idx = 0
while idx < len(s):
    if i % 2 == 0:
        for j in range(n):
            matrix[i][j] = s[idx]
            idx += 1
    else:
        for j in range(n-1, -1, -1):
            matrix[i][j] = s[idx]
            idx += 1
    i += 1
for i in range(n):
    for j in range(m):
        print(matrix[j][i], end='')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-07%20155259.png)



### M02092: Grandpa is Famous

implementation, http://cs101.openjudge.cn/practice/02092/



思路：



代码：

```python
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    rank = {}
    for _ in range(n):
        s = list(map(int, input().split()))
        for x in s:
            rank[x] = rank.get(x, 0) + 1
    lis = list((rank[x], x) for x in rank)
    lis.sort(key=lambda x:(-x[0], x[1]))
    ans = []
    for y in lis[1:]:
        if y[0] == lis[1][0]:
            ans.append(y[1])
    print(*ans)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-07%20163333.png)



### M04133: 垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/



思路：



代码：

```python
d = int(input())
n = int(input())
ans = {}
for _ in range(n):
    x, y, k = map(int, input().split())
    left = max(0, x - d)
    right = min(x + d, 1024)
    up = min(y + d, 1024)
    down = max(0, y - d)
    for i in range(left, right+1):
        for j in range(down, up+1):
            ans[(i, j)] = ans.get((i, j), 0) + k
out = {}
for key in ans:
    num = ans[key]
    out[num] = out.get(num, 0) + 1
max_out = max(out)
print(out[max_out], max_out)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-07%20155529.png)



### T02488: A Knight's Journey

backtracking, http://cs101.openjudge.cn/practice/02488/



思路：



代码：

```python
def dfs(lis=[('A', 1)]):
    if len(lis) == a*b:
        ans.append(''.join([x[0]+str(x[1]) for x in lis]))
        return
    y, x = ord(lis[-1][0]), lis[-1][1]
    for dx, dy in dire:
        nx, ny = x + dx, y + dy
        if 65 <= ny < 65+b and 1 <= nx <= a:
            if (chr(ny), nx) not in lis:
                dfs(lis+[(chr(ny), nx)])


dire = [(2, 1), (-2, 1), (1, -2), (1, 2), (2, -1), (-2, -1), (-1, -2), (-1, 2)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    ans = []
    dfs()
    ans.sort()
    print(f'Scenario #{i+1}:')
    if ans:
        print(ans[0])
    else:
        print('impossible')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-07%20190529.png)



### T06648: Sequence

heap, http://cs101.openjudge.cn/practice/06648/



思路：



代码：

```python
import heapq
t = int(input())


def merge(a, b):
    new = []
    heap = [(a[0] + b[i], 0, i) for i in range(n)]
    heapq.heapify(heap)
    for _ in range(n):
        num, j, i = heapq.heappop(heap)
        new.append(num)
        if j < n-1:
            heapq.heappush(heap, (a[j+1]+b[i], j+1, i))
    return new


for _ in range(t):
    m, n = map(int, input().split())
    ans = list(map(int, input().split()))
    ans.sort()
    for _ in range(m-1):
        a = list(map(int, input().split()))
        a.sort()
        ans = merge(ans, a)
    print(*ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-07%20203741.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

最后一题太难了:sob:










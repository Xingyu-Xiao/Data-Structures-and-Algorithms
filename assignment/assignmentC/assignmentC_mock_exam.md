# Assignment #C: 202505114 Mock Exam

Updated 1518 GMT+8 May 14, 2025

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

### E06364: 牛的选举

http://cs101.openjudge.cn/practice/06364/

思路：



代码：

```python
n, k = map(int, input().split())
a = [list(map(int, input().split()))+[1+i] for i in range(n)]
a.sort(reverse=True)
b = a[:k]
b.sort(key=lambda x: -x[1])
print(b[0][2])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-19%20095927.png)



### M04077: 出栈序列统计

http://cs101.openjudge.cn/practice/04077/

思路：



代码：

```python
n = int(input())
ans = 0


def dfs(stack=[],i=0,j=0):
    global ans
    if i == n:
        ans += 1
        return
    if stack:
        new_stack1 = stack[:len(stack)-1]
        dfs(new_stack1,i+1,j)
    if j < n:
        dfs(stack+[j],i,j+1)


dfs()
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-19%20104837.png)



### M05343:用队列对扑克牌排序

http://cs101.openjudge.cn/practice/05343/

思路：



代码：

```python
n = int(input())
s = input().split()
ans = []
dic = {'A':0,'B':1,'C':2,'D':3}
lis = ['A','B','C','D']
queue = [[] for i in range(9)]
for a in s:
    queue[int(a[1])-1].append(a)
queue_alpha = [[] for i in range(4)]
for i in range(9):
    print(f"Queue{i+1}:{' '.join(queue[i])}")
    for x in queue[i]:
        queue_alpha[dic[x[0]]].append(x)
for i in range(4):
    print(f"Queue{lis[i]}:{' '.join(queue_alpha[i])}")
    ans.extend(queue_alpha[i])
print(*ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-20%20093635.png)



### M04084: 拓扑排序

http://cs101.openjudge.cn/practice/04084/

思路：



代码：

```python
import heapq
v, a = map(int, input().split())
degree = [0]*v
dic = {i:[] for i in range(v)}
for i in range(a):
    x, y = map(int, input().split())
    degree[y-1] = degree[y-1] + 1
    dic[x-1].append(y)
ans = []
queue = []
for i in range(v):
    if degree[i] == 0:
        queue.append(i)
heapq.heapify(queue)
while queue:
    node = heapq.heappop(queue)
    ans.append(node)
    for y in dic[node]:
        degree[y-1] -= 1
        if degree[y-1] == 0:
            heapq.heappush(queue, y-1)
ans = ['v'+str(i+1) for i in ans]
print(*ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-20%20104447.png)



### M07735:道路

Dijkstra, http://cs101.openjudge.cn/practice/07735/

思路：



代码：

```python
import heapq
k = int(input())
n = int(input())
r = int(input())
adj = [[] for i in range(n+1)]
for i in range(r):
    s, d, l, t = map(int, input().split())
    adj[s].append((d,l,t))
distance = [{} for i in range(n+1)]
distance[1][0] = 0
queue = []
heapq.heappush(queue, (0, 1, 0))
while queue:
    length, city, cost = heapq.heappop(queue)
    if city == n:
        print(length)
        exit()
    if length > distance[city].get(cost, float('inf')):
        continue
    for (neighbor, l, t) in adj[city]:
        if cost + t > k:
            continue
        if cost+t in distance[neighbor]:
            if distance[neighbor][cost+t] <= length + l:
                continue
        distance[neighbor][cost+t] = length + l
        heapq.heappush(queue, (length+l, neighbor, cost + t))
print(-1)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-20%20144204.png)



### T24637:宝藏二叉树

dp, http://cs101.openjudge.cn/practice/24637/

思路：



代码：

```python
n = int(input())
s = list(map(int, input().split()))
dp = [[0]*(n+1),[s[i-1] for i in range(n+1)]]
for i in range(n//2,0,-1):
    left = i*2
    right = i*2+1 if i*2+1 <= n else 0
    r_max = max(dp[1][right], dp[0][right]) if right != 0 else 0
    dp[0][i] = max(dp[0][left], dp[1][left]) + r_max
    dp[1][i] = s[i-1] + dp[0][left] + dp[0][right]
print(max(dp[1][1], dp[0][1]))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-05-20%20162035.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

dijkstra算法还是不太熟练










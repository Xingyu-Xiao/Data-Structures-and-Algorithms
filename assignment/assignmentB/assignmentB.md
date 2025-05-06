# Assignment #B: 图为主

Updated 2223 GMT+8 Apr 29, 2025

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

### E07218:献给阿尔吉侬的花束

bfs, http://cs101.openjudge.cn/practice/07218/

思路：



代码：

```python
from collections import deque
dire = ((1, 0), (-1, 0), (0, 1), (0, -1))
t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    graph = [input() for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'S':
                start = (i, j)
                break

    def bfs(start):
        visited = set()
        visited.add(start)
        queue = deque([start])
        ans = 0
        while queue:
            new_queue = deque()
            ans += 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in dire:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visited and graph[nx][ny] != '#':
                        if graph[nx][ny] == 'E':
                            return ans
                        new_queue.append((nx, ny))
                        visited.add((nx, ny))
            queue = new_queue

    res = bfs(start)
    if res:
        print(res)
    else:
        print('oop!')


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](C:\Users\XXY13\Pictures\Screenshots\屏幕截图 2025-04-30 171123.png)



### M3532.针对图的路径存在性查询I

disjoint set, https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/

思路：



代码：

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        idx = []
        for i in range(n-1):
            if nums[i+1]-nums[i] > maxDiff:
                idx.append(i)
        return [bisect_left(idx, u) == bisect_left(idx, v) for u, v in queries]

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](C:\Users\XXY13\Pictures\Screenshots\屏幕截图 2025-05-06 134950.png)



### M22528:厚道的调分方法

binary search, http://cs101.openjudge.cn/practice/22528/

思路：



代码：

```python
points = list(map(float, input().split()))
points.sort()
min_point = points[int(len(points)*0.4)]
def new_point(b):
    return min_point*b/1000000000 + 1.1**(min_point*b/1000000000)

left, right = 0, 1000000000
while left < right:
    mid = (left+right)//2
    if new_point(mid) < 85:
        left = mid+1
    else:
        right = mid
print(right)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](C:\Users\XXY13\Pictures\Screenshots\屏幕截图 2025-05-06 164208.png)



### Msy382: 有向图判环 

dfs, https://sunnywhy.com/sfbj/10/3/382

思路：



代码：

```python
from collections import deque
n, m = map(int, input().split())
graph = {i:[] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    visited = set()
    visited.add(start)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == start:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


for node in graph.keys():
    ans = bfs(node)
    if ans:
        print('Yes')
        break
else:
    print('No')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](C:\Users\XXY13\Pictures\Screenshots\屏幕截图 2025-05-06 170922.png)



### M05443:兔子与樱花

Dijkstra, http://cs101.openjudge.cn/practice/05443/

思路：



代码：

```python
import heapq


def dijkstra(graph, start, end):
    # 初始化距离字典
    distances = {vertex: float('infinity') for vertex in graph}
    path = {vertex: '' for vertex in graph}
    path[start] = start
    distances[start] = 0
    # 使用优先队列
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 如果当前距离大于已记录的距离，跳过
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            # 如果找到更短路径，则更新
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = path[current_vertex] + f'->({weight})->'+neighbor
                heapq.heappush(priority_queue, (distance, neighbor))

    return path[end]


p = int(input())
graph = {}
for _ in range(p):
    graph[input()] = []
q = int(input())
for _ in range(q):
    start, end, weight = input().split()
    graph[start].append((end, int(weight)))
    graph[end].append((start, int(weight)))
r = int(input())
for _ in range(r):
    start, end = input().split()
    print(dijkstra(graph, start, end))


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](C:\Users\XXY13\Pictures\Screenshots\屏幕截图 2025-05-06 173937.png)



### T28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/

思路：



代码：

```python
n = int(input())
sr, sc = map(int, input().split())
dire = ((2, 1), (2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(-2,1),(-2,-1))
board=[[1]*n for i in range(n)]
board[sr][sc]=0


def dfs(start, i=1):
    if i == n**2:
        return True
    x, y = start
    nex = []
    for dx, dy in dire:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
            degree = 0
            for dx, dy in dire:
                nnx, nny = nx + dx, ny+dy
                if 0 <= nnx < n and 0 <= nny < n and board[nnx][nny]:
                    degree += 1
            nex.append((degree, nx, ny))
    nex.sort()
    for degree, x, y in nex:
        board[x][y] = 0
        if dfs((x, y),i+1):return True
        board[x][y] = 1

if dfs((sr, sc)):
    print('success')
else:
    print('fail')


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](C:\Users\XXY13\Pictures\Screenshots\屏幕截图 2025-05-06 204607.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

主要复习了dijkstra算法,学了**Warnsdorff优化**










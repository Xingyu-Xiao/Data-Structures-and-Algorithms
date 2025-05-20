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

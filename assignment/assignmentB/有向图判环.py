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

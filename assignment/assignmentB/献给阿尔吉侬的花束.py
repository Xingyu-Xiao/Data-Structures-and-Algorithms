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

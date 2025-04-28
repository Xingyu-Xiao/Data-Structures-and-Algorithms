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
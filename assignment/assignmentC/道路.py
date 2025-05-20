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


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


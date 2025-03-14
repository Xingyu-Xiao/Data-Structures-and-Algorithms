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

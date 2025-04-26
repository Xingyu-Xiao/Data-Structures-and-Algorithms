import heapq
n = int(input())
s = list(map(int, input().split()))
heapq.heapify(s)
ans = 0
while len(s) > 1:
    a = heapq.heappop(s)
    b = heapq.heappop(s)
    heapq.heappush(s, a+b)
    ans += (a+b)
print(ans)

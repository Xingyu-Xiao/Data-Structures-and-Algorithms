n, m = map(int, input().split())
A = [[0]*n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    A[a][a] += 1
    A[b][b] += 1
    A[a][b] -= 1
    A[b][a] -= 1
for x in A:
    print(*x)

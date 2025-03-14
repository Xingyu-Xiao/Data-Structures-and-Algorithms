while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    rank = {}
    for _ in range(n):
        s = list(map(int, input().split()))
        for x in s:
            rank[x] = rank.get(x, 0) + 1
    lis = list((rank[x], x) for x in rank)
    lis.sort(key=lambda x:(-x[0], x[1]))
    ans = []
    for y in lis[1:]:
        if y[0] == lis[1][0]:
            ans.append(y[1])
    print(*ans)


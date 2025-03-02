n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]


def check(cost):
    cnt = 0
    pre = 0
    for x in a:
        nex = x + pre
        if nex > cost:
            cnt += 1
            pre = x
        else:
            pre = nex
    cnt += 1
    return cnt <= m


left, right = max(a), sum(a)
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(right)

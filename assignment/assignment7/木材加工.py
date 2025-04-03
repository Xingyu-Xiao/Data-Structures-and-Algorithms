n, k = map(int, input().split())
log = [int(input()) for _ in range(n)]


def num(logs, length):
    number = 0
    for x in logs:
        number += (x // length)
    return number


left, right = 0, max(log)
while left < right - 1:
    mid = (left + right) // 2
    number = num(log, mid)
    if number >= k:
        left = mid
    else:
        right = mid
print(left)

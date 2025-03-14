d = int(input())
n = int(input())
ans = {}
for _ in range(n):
    x, y, k = map(int, input().split())
    left = max(0, x - d)
    right = min(x + d, 1024)
    up = min(y + d, 1024)
    down = max(0, y - d)
    for i in range(left, right+1):
        for j in range(down, up+1):
            ans[(i, j)] = ans.get((i, j), 0) + k
out = {}
for key in ans:
    num = ans[key]
    out[num] = out.get(num, 0) + 1
max_out = max(out)
print(out[max_out], max_out)

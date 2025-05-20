n = int(input())
s = list(map(int, input().split()))
dp = [[0]*(n+1),[s[i-1] for i in range(n+1)]]
for i in range(n//2,0,-1):
    left = i*2
    right = i*2+1 if i*2+1 <= n else 0
    r_max = max(dp[1][right], dp[0][right]) if right != 0 else 0
    dp[0][i] = max(dp[0][left], dp[1][left]) + r_max
    dp[1][i] = s[i-1] + dp[0][left] + dp[0][right]
print(max(dp[1][1], dp[0][1]))

t = int(input())
s = list(map(int, input().split()))
s.sort()
i, j = 0, len(s)-1
if t >= s[-1] + s[-2]:
    ans = s[-1] + s[-2]
elif t <= s[0] + s[1]:
    ans = s[0] + s[1]
else:
    res = []
    while i < j:
        tar = s[i]+s[j]
        if tar > t:
            j -= 1
        else:
            i += 1
        res.append((abs(t-tar), tar))
    res.sort()
    ans = res[0][1]
print(ans)

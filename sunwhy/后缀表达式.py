s = input().split()
ans = []
i = 0
while i < len(s):
    ss = s[i]
    if ss == '-' or ss == '+':
        ans.append(s[i+1])
        ans.append(ss)
        i += 2
    else:
        ans.append(ss)
        i += 1
print(' '.join(ans))

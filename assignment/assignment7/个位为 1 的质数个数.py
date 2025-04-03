t = int(input())
ns = [int(input()) for _ in range(t)]
n = max(ns)
s = [True]*(n+1)
num = []
for i in range(2,n+1):
    if s[i]:
        num.append(i)
    for j in range(i, n//i+1):
        s[j*i] = False
for i in range(t):
    ans = []
    for x in num:
        if str(x)[-1] == '1' and x < ns[i]:
            ans.append(x)
    print(f'Case{i+1}:')
    if ans:
        print(*ans)
    else:
        print('NULL')

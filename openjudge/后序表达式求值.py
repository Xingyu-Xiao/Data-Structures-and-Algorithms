n = int(input())
s = ['+', '-', '*', '/']
for _ in range(n):
    a = input().split()
    ans = []
    for x in a:
        if x in s:
            q = ans.pop()
            p = ans.pop()
            if x == s[0]:
                ans.append(p+q)
            elif x == s[1]:
                ans.append(p-q)
            elif x == s[2]:
                ans.append(p*q)
            else:
                ans.append(p/q)
        else:
            ans.append(float(x))
    print(f'{ans[0]:.2f}')

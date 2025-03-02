s = []
ss = []
for o in range(3):
    row, col = map(int, input().split())
    s.append([row, col])
    p = []
    for i in range(row):
        p.append(list(map(int, input().split())))
    ss.append(p)
if s[0][1] != s[1][0]:
    print('Error!')
else:
    if s[0][0] != s[2][0] or s[1][1] != s[2][1]:
        print('Error!')
    else:
        a = ss[0]
        b = ss[1]
        c = ss[2]
        for i in range(len(a)):
            for j in range(s[1][1]):
                dij = 0
                for k in range(len(b)):
                    dij += a[i][k]*b[k][j]
                c[i][j] += dij
        for y in c:
            print(' '.join(map(str, y)))

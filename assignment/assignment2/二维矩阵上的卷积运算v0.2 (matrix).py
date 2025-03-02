m, n, p, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
core = [list(map(int, input().split())) for _ in range(p)]


def f(i, j):
    s = []
    for k in range(p):
        for o in range(q):
            s.append(matrix[k+i][o+j]*core[k][o])
    return sum(s)


for i in range(m-p+1):
    out = []
    for j in range(n-q+1):
        out.append(f(i, j))
    print(' '.join(map(str, out)))

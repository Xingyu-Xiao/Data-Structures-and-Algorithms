n = int(input())
s = input()
m = len(s)//n
matrix = [['' for _ in range(n)] for _ in range(m)]
i = 0
idx = 0
while idx < len(s):
    if i % 2 == 0:
        for j in range(n):
            matrix[i][j] = s[idx]
            idx += 1
    else:
        for j in range(n-1, -1, -1):
            matrix[i][j] = s[idx]
            idx += 1
    i += 1
for i in range(n):
    for j in range(m):
        print(matrix[j][i], end='')

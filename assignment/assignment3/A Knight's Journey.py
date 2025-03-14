def dfs(lis=[('A', 1)]):
    if len(lis) == a*b:
        ans.append(''.join([x[0]+str(x[1]) for x in lis]))
        return
    y, x = ord(lis[-1][0]), lis[-1][1]
    for dx, dy in dire:
        nx, ny = x + dx, y + dy
        if 65 <= ny < 65+b and 1 <= nx <= a:
            if (chr(ny), nx) not in lis:
                dfs(lis+[(chr(ny), nx)])


dire = [(2, 1), (-2, 1), (1, -2), (1, 2), (2, -1), (-2, -1), (-1, -2), (-1, 2)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    ans = []
    dfs()
    ans.sort()
    print(f'Scenario #{i+1}:')
    if ans:
        print(ans[0])
    else:
        print('impossible')
    print()
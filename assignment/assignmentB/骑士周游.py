n = int(input())
sr, sc = map(int, input().split())
dire = ((2, 1), (2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(-2,1),(-2,-1))
board=[[1]*n for i in range(n)]
board[sr][sc]=0


def dfs(start, i=1):
    if i == n**2:
        return True
    x, y = start
    nex = []
    for dx, dy in dire:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
            degree = 0
            for dx, dy in dire:
                nnx, nny = nx + dx, ny+dy
                if 0 <= nnx < n and 0 <= nny < n and board[nnx][nny]:
                    degree += 1
            nex.append((degree, nx, ny))
    nex.sort()
    for degree, x, y in nex:
        board[x][y] = 0
        if dfs((x, y),i+1):return True
        board[x][y] = 1

if dfs((sr, sc)):
    print('success')
else:
    print('fail')


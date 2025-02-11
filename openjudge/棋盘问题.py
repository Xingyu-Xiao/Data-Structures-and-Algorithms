while True:
    n, k = map(int, input().split())
    if n == k == -1:
        break
    board = [list(input()) for _ in range(n)]
    num = 0
    visited = [True]*n


    def dfs(idx=0, c=0):
        global num
        if idx == k:
            num += 1
            return
        if c == n:
            return
        for j in range(c, n):
            for i in range(n):
                if board[i][j] == '#' and visited[i]:
                    visited[i] = False
                    dfs(idx+1, j+1)
                    visited[i] = True
    dfs()
    print(num)

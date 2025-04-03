from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = []
        n, m = len(board), len(board[0])
        k = len(word)
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    starts.append((i, j))
        ans = False
        dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(start, idx=0):
            nonlocal ans
            if idx == k-1:
                ans = True
                return
            x, y = start
            for dx, dy in dire:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited.get((nx, ny), 0):
                    if board[nx][ny] == word[idx+1]:
                        visited[(nx, ny)] = 1
                        dfs((nx, ny), idx+1)
                        visited[(nx, ny)] = 0

        for start in starts:
            visited = {}
            visited[start] = 1
            dfs(start)
        return ans

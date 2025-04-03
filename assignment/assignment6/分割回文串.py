from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i+1, n+1):
                t = s[i:j]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j)
                    path.pop()

        dfs(0)
        return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = ['']*n
        def dfs(i=0):
            if i == n:
                ans.append(''.join(path))
                return
            for c in mapping[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs()
        return ans


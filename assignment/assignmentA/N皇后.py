class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen = ['.']*n
        ans = []
        judge = [True]*n
        diag1 = [True]*(2*n-1)
        diag2 = [True]*(2*n-1)
        def dfs(lis=[],j=0):
            if j == n:
                ans.append(lis)
                return
            for i in range(n):
                if judge[i] and diag1[i+j] and diag2[i-j+n-1]:
                    judge[i] = False
                    diag1[i+j] = False
                    diag2[i-j+n-1] = False
                    dfs(lis+[i],j+1)
                    judge[i] = True
                    diag1[i+j] = True
                    diag2[i-j+n-1] = True
        dfs()
        for i in range(len(ans)):
            x = []
            for j in range(n):
                y = queen.copy()
                y[ans[i][j]] = 'Q'
                x.append(''.join(y))
            ans[i] = x
        return ans
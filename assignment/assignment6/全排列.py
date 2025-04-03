from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        p = [True]*n
        ans = []

        def dfs(lis=[], idx=0):
            if idx == n:
                ans.append(lis)
            for i in range(n):
                if p[i]:
                    p[i] = False
                    dfs(lis+[nums[i]], idx+1)
                    p[i] = True

        dfs()
        return ans
    
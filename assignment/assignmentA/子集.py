class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        p = [True] * len(nums)

        def backtrack(n, res=[], i=0):
            if i == n:
                res.sort()
                ans.add(tuple(res))
                return
            for j in range(len(nums)):
                if p[j]:
                    p[j] = False
                    backtrack(n, res + [nums[j]], i + 1)
                    p[j] = True

        for k in range(len(nums)):
            backtrack(k)

        ans = list(set(ans))
        for i in range(len(ans)):
            ans[i] = list(ans[i])
        ans.append(nums)
        return ans

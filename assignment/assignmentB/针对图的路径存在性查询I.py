class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        idx = []
        for i in range(n-1):
            if nums[i+1]-nums[i] > maxDiff:
                idx.append(i)
        return [bisect_left(idx, u) == bisect_left(idx, v) for u, v in queries]

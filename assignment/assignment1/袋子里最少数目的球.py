from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(m):
            cnt = 0
            for num in nums:
                cnt += (num - 1) // m
            return cnt <= maxOperations

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return right

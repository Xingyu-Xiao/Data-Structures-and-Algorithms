from typing import List
from heapq import heappop
from heapq import heappush


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        a = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))
        n = len(a)
        ans = [0]*n
        s = []
        pre = a[0][0]
        o = 0
        temp = []
        out = 0
        heappush(temp, a[0][1])
        for i in range(1, n):
            j = a[i][2]
            if a[i][0] == pre:
                ans[j] = ans[o]
                heappush(temp, a[i][1])
                continue
            pre = a[i][0]
            o = j
            while temp:
                x = heappop(temp)
                heappush(s, x)
                out += x
            while len(s) > k:
                out -= heappop(s)
            ans[j] = out
            heappush(temp, a[i][1])
        return ans


a = eval(input())
b = eval(input())
k = int(input())
print(Solution().findMaxSum(a, b, k))

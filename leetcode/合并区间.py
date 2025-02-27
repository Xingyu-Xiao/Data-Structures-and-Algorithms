from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = []
        pre = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= pre[1]:
                pre = [pre[0], max(interval[1], pre[1])]
            else:
                ans.append(pre)
                pre = interval
        ans.append(pre)
        return ans

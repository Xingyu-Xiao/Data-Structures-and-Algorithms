from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        n = 0
        while n < numRows-1:
            tem = [1]
            for i in range(n):
                tem.append(ans[-1][i]+ans[-1][i+1])
            tem.append(1)
            ans.append(tem)
            n += 1
        return ans

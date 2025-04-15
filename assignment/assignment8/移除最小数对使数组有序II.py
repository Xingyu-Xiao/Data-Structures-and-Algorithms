from typing import List
import heapq


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        class Node:
            def __init__(self, left, right, idx):
                self.pre = None
                self.left = left
                self.right = right
                self.idx = idx
                self.next = None

        n = len(nums)
        if n <= 1:
            return 0
        head = Node(nums[0], nums[1], 0)
        pr = head
        node_dic = {0: head}
        dec = 0 if nums[0] <= nums[1] else 1
        h = [(nums[0]+nums[1], 0)]
        for i in range(1, n-1):
            nxt = Node(nums[i], nums[i+1], i)
            node_dic[i] = nxt
            pr.next = nxt
            nxt.pre = pr
            pr = nxt

            x, y = nums[i], nums[i+1]
            h.append((x+y, i))
            if x > y:
                dec += 1
        heapq.heapify(h)

        ans = 0
        judge = [False]*(n-1)
        while dec:
            ans += 1
            new_val, idx = heapq.heappop(h)
            node = node_dic[idx]
            while node.right + node.left != new_val or judge[idx]:
                new_val, idx = heapq.heappop(h)
                node = node_dic[idx]
            judge[idx] = True
            if node.left > node.right:
                dec -= 1
            next_node = node.next
            pre_node = node.pre
            if next_node:
                if new_val > next_node.right:
                    dec += 1
                if next_node.left > next_node.right:
                    dec -= 1
                next_node.left = new_val
                next_node.pre = pre_node
                nxt_val = next_node.left + next_node.right
                nex_idx = next_node.idx
                heapq.heappush(h, (nxt_val, nex_idx))

            if pre_node:
                if pre_node.left > pre_node.right:
                    dec -= 1
                if new_val < pre_node.left:
                    dec += 1
                pre_node.right = new_val
                pre_node.next = next_node
                pre_val = pre_node.right + pre_node.left
                pre_idx = pre_node.idx
                heapq.heappush(h, (pre_val, pre_idx))

        return ans


nums = eval(input())
print(Solution.minimumPairRemoval(None, nums))

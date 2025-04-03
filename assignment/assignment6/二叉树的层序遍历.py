from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]

        def dfs(stack=[root]):
            stack = deque(stack)
            nex = []
            while stack:
                node = stack.popleft()
                if node is not None:
                    if node.left is not None:
                        nex.append(node.left)
                    if node.right is not None:
                        nex.append(node.right)
            if not nex:
                return
            val_nex = [node.val for node in nex]
            ans.append(val_nex)
            dfs(nex)

        dfs()
        return ans
    
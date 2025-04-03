# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(True, root)]
        ans = []
        while stack:
            judge, node = stack.pop()
            if node is None:
                continue
            if judge:
                stack.append((True, node.right))
                stack.append((False, node))
                stack.append((True, node.left))
            else:
                ans.append(node.val)
        return ans
    
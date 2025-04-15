class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        def dfs(node, s):
            if node.left is None and node.right is None:
                ans.append(int(s))
                return
            if node.left is not None:
                dfs(node.left, s+str(node.left.val))
            if node.right is not None:
                dfs(node.right, s+str(node.right.val))

        dfs(root, str(root.val))
        return sum(ans)

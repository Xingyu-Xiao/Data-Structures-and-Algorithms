class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]

        def dfs(stack=[root], i=0):
            nex = []
            if i % 2 == 0:
                while stack:
                    node = stack.pop()
                    if node is not None:
                        if node.right is not None:
                            nex.append(node.right)
                        if node.left is not None:
                            nex.append(node.left)
                if not nex:
                    return
                val_nex = [node.val for node in nex]
                ans.append(val_nex)
            else:
                while stack:
                    node = stack.pop()
                    if node is not None:
                        if node.left is not None:
                            nex.append(node.left)
                        if node.right is not None:
                            nex.append(node.right)
                if not nex:
                    return
                val_nex = [node.val for node in nex]
                ans.append(val_nex)

            dfs(nex, i + 1)

        dfs()
        return ans

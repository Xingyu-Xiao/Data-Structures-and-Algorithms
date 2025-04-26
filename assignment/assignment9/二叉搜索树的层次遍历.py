from collections import deque
s = list(map(int, input().split()))


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)
    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


a = {s[0]}
root = Node(s[0])
for x in s[1:]:
    if x in a:
        continue
    insert(root, x)
    a.add(x)
ans = [s[0]]


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
    ans.extend(val_nex)
    dfs(nex)


dfs()
print(*ans)

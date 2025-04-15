class TreeNode:
    def __init__(self, val):
        self.children = []
        self.par = None
        self.val = val


Node_dic = {}
n = int(input())
for _ in range(n):
    nodes = list(map(int, input().split()))
    if nodes[0] not in Node_dic:
        one = TreeNode(nodes[0])
        Node_dic[nodes[0]] = one
    else:
        one = Node_dic[nodes[0]]
    for node in nodes[1:]:
        if node not in Node_dic:
            nod = TreeNode(node)
            Node_dic[node] = nod
        else:
            nod = Node_dic[node]
        one.children.append(nod)
        nod.par = one

for node in Node_dic.values():
    if node.par is None:
        root = node

stack = [(True, root)]
ans = []
while stack:
    judge, node = stack.pop()
    if node is None:
        continue
    if judge:
        lis = node.children + [node]
        lis.sort(key=lambda x: x.val)
        for x in lis:
            if x == node:
                stack.append((False, x))
            else:
                stack.append((True, x))
    else:
        ans.append(node.val)
while ans:
    print(ans.pop())

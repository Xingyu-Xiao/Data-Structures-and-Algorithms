class Tree:
    def __init__(self, name):
        self.children = []
        self.name = name


def printTree(root):
    stack = [(True, root)]
    ans = []
    while stack:
        judge, node = stack.pop()
        if node is None:
            continue
        if judge:
            stack.append((False, node))
            for child in node.children[::-1]:
                stack.append((True, child))
        else:
            ans.append(node.name)
    return ans


n = int(input())
out = []
for _ in range(n):
    inp = input().split()
    nu = [inp[i] for i in range(len(inp)) if i % 2 == 1]
    nodes = [Tree(x) for x in inp if x not in nu]
    num = list(map(int, nu))
    idx = num[0]
    root = nodes[0]
    root.children.extend(nodes[1:num[0]+1])
    for i in range(1, len(nu)):
        node = nodes[i]
        node.children.extend(nodes[idx+1:idx+1+num[i]])
        idx += num[i]
    out.extend(printTree(root))
print(*out)

import heapq


class Node:
    def __init__(self, weight, char=None):
        self.char = char
        self.weight = weight
        self.left = None
        self.right = None

    def __lt__(self, other):
        return (self.weight, self.char) < (other.weight, other.char)


def build_tree(characters):
    heap = []
    for char, weight in characters:
        heapq.heappush(heap, Node(weight, char))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.weight + right.weight)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]


def encode(root):
    codes = {}

    def traverse(node, code=''):
        if not node.left and not node.right:
            codes[node.char] = code
            return
        traverse(node.left, code+'0')
        traverse(node.right, code+'1')

    traverse(root)
    return codes


def add_code(string, codes):
    addcode = ''
    for c in string:
        addcode += codes[c]
    return addcode


def decode(root, code):
    string = ''
    node = root
    for bit in code:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            string += node.char
            node = root
    return string


n = int(input())
characters = []
for _ in range(n):
    char, weight = input().split()
    characters.append((char, int(weight)))
root = build_tree(characters)
codes = encode(root)

while True:
    try:
        s = input()
        if s[0] in ('1', '0'):
            print(decode(root, s))
        else:
            print(add_code(s, codes))
    except EOFError:
        break

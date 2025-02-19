class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        self.size += 1
        if self.tail is None:
            self.tail = node
            self.tail.next = self.tail
        else:
            p = self.tail.next
            self.tail.next = node
            node.next = p
        self.tail = self.tail.next

    def remove(self, m):
        one = self.tail
        for _ in range(m-1):
            one = one.next
        one.next = one.next.next
        self.size -= 1
        self.tail = one


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    cir = LinkedList()
    for _ in range(1, n+1):
        cir.append(_)
    for _ in range(n-1):
        cir.remove(m)
    print(cir.tail.data)

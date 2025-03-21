from collections import deque


def hot_potato(name_list, num):
    ans = []
    queue = deque()
    for name in name_list:
        queue.append(name)

    while len(queue) > 0:
        for i in range(num):
            queue.append(queue.popleft())
        ans.append(queue.popleft())
    return ans


while True:
    n, p, m = map(int, input().split())
    if {n,m, p} == {0}:
        break
    monkey = [i for i in range(p, n+1)] + [i for i in range(1, p)]
    print(','.join(map(str, hot_potato(monkey, m-1))))


'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.tail = None

    def append(self, data):
        node = Node(data)
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
        re = one.next.data
        one.next = one.next.next
        self.tail = one
        return re


while True:
    ans = []
    n, p, m = map(int, input().split())
    if n == p == m == 0:
        break
    cir = LinkedList()
    for i in range(p, n+1):
        cir.append(i)
    for i in range(1, p):
        cir.append(i)
    for i in range(n):
        ans.append(cir.remove(m))
    print(','.join(map(str, ans)))
'''
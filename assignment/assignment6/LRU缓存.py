class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.nex = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.tail = Node()
        self.head = Node()
        self.head.nex, self.tail.pre = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        node.pre.nex, node.nex.pre = node.nex, node.pre
        tail_pre = self.tail.pre
        tail_pre.nex, self.tail.pre, node.pre, node.nex = node, node, tail_pre, self.tail
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.pre.nex, node.nex.pre = node.nex, node.pre
        node = Node(key, value)
        tail_pre = self.tail.pre
        tail_pre.nex, self.tail.pre, node.pre, node.nex = node, node, tail_pre, self.tail
        self.key_to_node[key] = node
        if len(self.key_to_node) > self.capacity:
            last_node = self.head.nex
            del self.key_to_node[last_node.key]
            self.head.nex, last_node.nex.pre = last_node.nex, self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
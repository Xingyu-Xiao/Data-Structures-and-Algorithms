class Binaryheap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2
            if self.heap[i] < self.heap[parent_idx]:
                self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
                i = parent_idx
            else:
                break

    def pop(self):
        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]
        res = heap.pop()
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left
            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        return res


n = int(input())
heapq = Binaryheap()
for _ in range(n):
    s = input().split()
    if s[0] == '2':
        print(heapq.pop())
    else:
        heapq.push(int(s[1]))

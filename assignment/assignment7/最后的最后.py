from collections import deque


def f(name_list, num):
    ans = []
    queue = deque(name_list)

    while len(queue) > 0:
        for i in range(num):
            queue.append(queue.popleft())
        ans.append(queue.popleft())
    ans.pop()
    return ans


n, m = map(int, input().split())
s = [i for i in range(1, n+1)]
print(' '.join(map(str, f(s, m-1))))

from collections import deque
import bisect
n = int(input())
queue = deque()
lis = []
for _ in range(n):
    s = input().split()
    if s[0] == 'add':
        queue.append(int(s[1]))
        bisect.insort(lis, int(s[1]))
    elif s[0] == 'del':
        a = queue.popleft()
        idx = bisect.bisect_left(lis, a)
        lis.pop(idx)
    else:
        length = len(queue)
        if length % 2 == 0:
            ans_2 = lis[length//2]+lis[length//2-1]
            if ans_2 % 2 != 0:
                print(f'{ans_2/2:.1f}')
            else:
                print(ans_2//2)
        else:
            print(lis[length//2])

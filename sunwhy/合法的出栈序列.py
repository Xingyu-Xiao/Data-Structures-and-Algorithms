n = int(input())
s = list(map(int, input().split()))
stack = []
j = 0
for i in range(1, n+1):
    stack.append(i)
    while stack and s[j] == stack[-1]:
        stack.pop()
        j += 1
if not stack and j == n:
    print('Yes')
else:
    print('No')

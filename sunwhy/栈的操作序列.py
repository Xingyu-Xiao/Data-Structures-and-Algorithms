n = int(input())
stack = []
for i in range(n):
    p = input()
    if p == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    else:
        num = p.split()[-1]
        stack.append(num)

output = []
n = int(input())


def generate(pre_stack, stack, out_stack):
    if not pre_stack and not stack:
        output.append(out_stack)
    if pre_stack:
        generate(pre_stack[1:], stack + [pre_stack[0]], out_stack)
    if stack:
        generate(pre_stack, stack[:-1], out_stack + [stack[-1]])


generate([i for i in range(1, n+1)], [], [])
output.sort()
for x in output:
    print(*x)

def solve(pre, ino):
    if not pre:
        return ''
    root = pre[0]
    idx = ino.index(root)
    left_ino = ino[:idx]
    right_ino = ino[idx+1:]
    left_pre = pre[1:idx+1]
    right_pre = pre[idx+1:]
    return solve(left_pre, left_ino) + solve(right_pre, right_ino) + root


while True:
    try:
        pre = input()
        ino = input()
        print(solve(pre, ino))
    except EOFError:
        break

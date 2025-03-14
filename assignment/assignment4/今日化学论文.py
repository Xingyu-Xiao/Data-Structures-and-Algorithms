a = input()
while '[' in a:
    idx = a.index('[')
    n = ''
    idx3 = 0
    for i in range(idx+1, len(a)):
        if a[i].isdigit():
            n += a[i]
        else:
            idx3 = i
            break
    n = int(n)
    m = 1
    idx2 = 0
    for i, x in enumerate(a[idx+2:]):
        if x == '[':
            m += 1
        if x == ']':
            m -= 1
            if m == 0:
                idx2 = i + idx + 2
                break
    a = a[:idx] + a[idx3:idx2]*n + a[idx2+1:]
print(a)

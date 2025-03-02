n = int(input())
ans = {}
for i in range(n):
    name, scale = input().split('-')
    if name in ans:
        ans[name] = ans[name] + [scale]
    else:
        ans[name] = [scale]
out = [(key, ans[key]) for key in ans]
out.sort()
for name, scales in out:
    b = [x for x in scales if x[-1] == 'B']
    m = [x for x in scales if x[-1] == 'M']
    b.sort(key=lambda x: float(x[:-1]))
    m.sort(key=lambda x: float(x[:-1]))
    print(name, end=': ')
    if m:
        if b:
            print(', '.join(m), end=', ')
        else:
            print(', '.join(m))
    if b:
        print(', '.join(b))


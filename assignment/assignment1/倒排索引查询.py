n = int(input())
max_num = 0
dic = dict()
for i in range(n):
    s = list(map(int, input().split()))
    dic[i] = s[1:]
    max_num = max(max_num, max(s[1:]))
m = int(input())


def found(j):
    return set(dic[j])


def not_found(j):
    al = set([i for i in range(1, max_num+1)])
    return al.difference(set(dic[j]))


for _ in range(m):
    s = map(int, input().split())
    ans = set([i for i in range(1, max_num+1)])
    for idx, x in enumerate(s):
        if x == 1:
            ans.intersection_update(found(idx))
        if x == -1:
            ans.intersection_update(not_found(idx))
    ans = list(ans)
    ans.sort()
    if ans:
        print(*ans)
    else:
        print('NOT FOUND')

n = int(input())
dic = dict()
for i in range(n):
    s = input().split()
    for word in s[1:]:
        if word in dic:
            if dic[word][-1] == i+1:
                continue
            dic[word] = dic[word] + [i+1]
        else:
            dic[word] = [i+1]
m = int(input())
for i in range(m):
    s = input()
    if s in dic:
        print(*dic[s])
    else:
        print('NOT FOUND')

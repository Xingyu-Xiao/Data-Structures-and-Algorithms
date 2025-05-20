n = int(input())
s = input().split()
ans = []
dic = {'A':0,'B':1,'C':2,'D':3}
lis = ['A','B','C','D']
queue = [[] for i in range(9)]
for a in s:
    queue[int(a[1])-1].append(a)
queue_alpha = [[] for i in range(4)]
for i in range(9):
    print(f"Queue{i+1}:{' '.join(queue[i])}")
    for x in queue[i]:
        queue_alpha[dic[x[0]]].append(x)
for i in range(4):
    print(f"Queue{lis[i]}:{' '.join(queue_alpha[i])}")
    ans.extend(queue_alpha[i])
print(*ans)

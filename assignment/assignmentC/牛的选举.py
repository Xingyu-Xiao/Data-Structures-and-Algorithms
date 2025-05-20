n, k = map(int, input().split())
a = [list(map(int, input().split()))+[1+i] for i in range(n)]
a.sort(reverse=True)
b = a[:k]
b.sort(key=lambda x: -x[1])
print(b[0][2])

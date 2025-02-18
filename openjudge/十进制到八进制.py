a = int(input())
ans = ''
while a > 0:
    ans = str(a % 8) + ans
    a = a // 8
print(ans)

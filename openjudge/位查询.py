MOD = 65536
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    a, b = input().split()
    if a == 'Q':
        num = 0
        for x in arr:
            bin_x = bin(x)
            if bin_x[-int(b)-1] == '1' and len(bin_x)-2 >= int(b):
                num += 1
        print(num)
    else:
        arr = list(map(lambda x: (x+int(b))%MOD, arr))

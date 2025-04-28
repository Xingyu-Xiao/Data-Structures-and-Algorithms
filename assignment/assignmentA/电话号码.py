n = int(input())
for _ in range(n):
    m = int(input())
    phonenumbers = [input() for _ in range(m)]
    phonenumbers.sort()
    for i in range(len(phonenumbers)-1):
        if phonenumbers[i] == phonenumbers[i+1][:len(phonenumbers[i])]:
            print('NO')
            break
    else:
        print('YES')

def check(a):
    num = a.count('@')
    if num != 1:
        return 'NO'
    if a[0] == '@' or a[0] == '.':
        return 'NO'
    if a[-1] == '@' or a[-1] == '.':
        return 'NO'
    idx = a.index('@')
    if a[idx-1] == '.' or a[idx+1] == '.':
        return 'NO'
    if '.' not in a[idx+2:]:
        return 'NO'
    return 'YES'


while True:
    try:
        s = input()
        print(check(s))
    except EOFError:
        break

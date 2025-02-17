while True:
    try:
        s = input()
        ans = []
        stack = []
        idx = []
        for index, char in enumerate(s):
            if char == '(':
                stack.append(char)
                ans.append(' ')
                idx.append(index)
            elif char == ')':
                if stack:
                    stack.pop()
                    idx.pop()
                    ans.append(' ')
                else:
                    ans.append('?')
            else:
                ans.append(' ')
        for i in idx:
            ans[i] = '$'
        print(s)
        print(''.join(ans))
    except EOFError:
        break

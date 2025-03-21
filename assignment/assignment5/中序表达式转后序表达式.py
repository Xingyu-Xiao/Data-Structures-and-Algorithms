n = int(input())
precedence = {'*': 1, '/': 1, '+': 0, '-': 0, '(': -1}


def convert(s):
    stack = []
    output = []
    temp = ''
    for char in s:
        if char.isdigit():
            temp += char
        elif char == '.':
            temp += '.'
        elif char == '(':
            stack.append('(')
        elif char == ')':
            if temp:
                output.append(temp)
            temp = ''
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            if temp:
                output.append(temp)
            temp = ''
            while stack and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
    if temp:
        output.append(temp)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)


for _ in range(n):
    s = input().strip()
    print(convert(s))

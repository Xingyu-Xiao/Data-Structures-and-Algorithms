tree = input()
pre = tree.replace('(', '').replace(')', '').replace(',', '')
stack = []
beh = []
for char in tree:
    if char.isalpha():
        stack.append(char)
    if char == ')' or char == ',':
        beh.append(stack.pop())
beh.append(stack.pop())
print(pre)
print(''.join(beh))

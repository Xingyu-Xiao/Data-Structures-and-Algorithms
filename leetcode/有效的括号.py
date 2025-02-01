class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        else:
            stack = []
            for char in s:
                if char in ['(', '{', '[']:
                    stack.append(char)
                else:
                    if char == ')':
                        if stack and stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    if char == ']':
                        if stack and stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    if char == '}':
                        if stack and stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
            if len(stack) == 0:
                return True
            else:
                return False


s = input()
print(Solution().isValid(s))

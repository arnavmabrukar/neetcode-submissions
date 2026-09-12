class Solution:
    def isValid(self, s: str) -> bool:
        syntax = {')':'(', '}':'{', ']':'['}
        stack = deque()

        for i in s:
            if i in syntax: #closing
                if stack and stack[-1] == syntax[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

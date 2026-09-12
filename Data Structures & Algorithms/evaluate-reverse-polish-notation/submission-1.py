class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if number push in stack
        # if arithmatic complete the corresponding operating between each item in the stack
        # once arithmatic done clear the stack
        # we are going to use a current number to update the oprations done on it
        stack = []
        for c in tokens:
            if c == '+':
                a,b = stack.pop(), stack.pop()
                stack.append(int(a+b))
            elif c == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b-a))
            elif c == '*':
                a,b = stack.pop(), stack.pop()
                stack.append(int(a*b))
            elif c == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                # a number
                stack.append(int(c))
        return stack[0]

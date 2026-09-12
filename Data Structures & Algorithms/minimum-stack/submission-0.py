class MinStack:

    def __init__(self):
        self.stack = [] # init a normal stack
        self.minStack = [] # for tracking minimum

    def push(self, val: int) -> None:
        self.stack.append(val) # append the val
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

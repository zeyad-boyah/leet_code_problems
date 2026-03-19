class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum:
            if val <= self.minimum[-1]:
                self.minimum.append(val)
        else:
            self.minimum.append(val)
            

    def pop(self) -> None:
        temp_val = self.stack.pop()
        if temp_val == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minimum[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(-2)
minStack.push(-3)
minStack.push(-3)
minStack.getMin() 
minStack.pop()
minStack.getMin()
# minStack.pop()
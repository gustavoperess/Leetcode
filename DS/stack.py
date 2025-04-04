class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)

    def pop(self) -> None:
        if self.isEmpty():
            return "Stack is Empty"
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
        
    def printStack(self):
        return print(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def getMin(self) -> int:
        return self.minStack[-1]




minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
t = minStack.top()  
print(t)
minStack.printStack()
minStack.pop()
minStack.printStack()
x = minStack.getMin() 
print(x)

 
# minStack.getMin()

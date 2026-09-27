class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.minarr = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.min = val
            self.minarr.append(val)

    def pop(self) -> None:
        top = self.top()
        if top == self.min:
            self.minarr = self.minarr[:-1]
            if self.minarr:
                self.min = self.minarr[-1]
            else:
                self.min = float('inf')
        self.stack = self.stack[:-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

        

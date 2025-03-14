class StackList:
    def __init__(self, value):
        self.stack = [value]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
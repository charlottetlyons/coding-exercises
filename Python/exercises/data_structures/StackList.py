class StackList:
    def __init__(self):
        self.stack = []

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

    def sort_stack(self):
        sorted_stack = StackList()

        while len(self.stack) != 0:
            temp = self.pop()

            while not len(sorted_stack.stack) == 0 and sorted_stack.peek() > temp:
                self.push(sorted_stack.pop())
            sorted_stack.push(temp)

        while len(sorted_stack.stack) != 0:
            self.push(sorted_stack.pop())
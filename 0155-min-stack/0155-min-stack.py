class MinStack:

    def __init__(self):
        self.stack = []
        self.min_v = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_v:
            min_v = min(val, self.getMin())
        else:
            min_v = val
        self.min_v.append(min_v)

    def pop(self) -> None:
        self.stack.pop()
        self.min_v.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_v[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
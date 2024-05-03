class MinStack:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.stack_min: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.stack_min[-1] if self.stack_min else val)
        self.stack_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return not self.stack

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        # check if null
        if self.isEmpty(): return
        last_el = self.stack[-1]
        del self.stack[-1]
        return last_el

    def top(self) -> int:
        if self.isEmpty(): return
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

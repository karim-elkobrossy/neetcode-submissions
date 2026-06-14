import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack: self.min_stack.append(val)
        else: self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # check if null
        last_el = self.stack[-1]
        del self.stack[-1]
        del self.min_stack[-1]
        return last_el

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

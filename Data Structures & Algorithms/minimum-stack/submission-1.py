class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack: return None
        del self.stack[-1]

    def top(self) -> int:
        if not self.stack: return None
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack) if self.stack else None
stack = MinStack()


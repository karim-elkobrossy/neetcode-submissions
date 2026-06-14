class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimums=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimums)>0:
            if val<=self.minimums[-1]: 
                self.minimums.append(val)
        else: self.minimums.append(val)

    def pop(self) -> None:
        if not self.stack: return None
        if len(self.minimums)>0 and self.minimums[-1]==self.stack[-1]: 
            del self.minimums[-1]
        del self.stack[-1]

    def top(self) -> int:
        if not self.stack: return None
        return self.stack[-1]

    def getMin(self) -> int:
        return None if len(self.minimums)==0 else self.minimums[-1]

stack = MinStack()


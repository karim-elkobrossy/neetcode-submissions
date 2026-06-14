from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations={'+', '-', '*', '/'}
        stack=deque()
        for el in tokens:
            if el not in operations: stack.append(int(el))
            else:
                el2=stack.pop()
                el1=stack.pop()
                print(el1, el2)
                if el=='+': stack.append(el1+el2)
                elif el=='-': stack.append(el1-el2)
                elif el=='/': stack.append(int(el1 / el2))
                elif el=='*': stack.append(el1*el2)
        return stack.pop() if stack else None
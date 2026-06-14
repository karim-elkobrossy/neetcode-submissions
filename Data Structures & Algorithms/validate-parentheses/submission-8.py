from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = {"(", "{", "["}
        closed_open_map = {")": "(", "}": "{", "]": "["}
        for symb in s:
            print(symb)
            if symb in open_brackets:
                stack.append(symb)
            else:
                if not stack: return False
                last_open = stack.pop()
                # Stack order and equivalence of open-closed brackets
                if last_open != closed_open_map[symb]:
                    return False 
        # If the stack still has elements, then return False
        if stack: return False
        return True
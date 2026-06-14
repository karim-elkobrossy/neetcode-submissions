class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2: return False
        stack = deque()
        dct_close_open={')':'(', '}':'{', ']':'['}
        for c in s:
            # Fill in the stack until you find the first closed paranthesis
            if c not in dct_close_open: stack.append(c)
            else: 
                try: last_paranthesis = stack.pop()
                except: return False
                if dct_close_open[c]!=last_paranthesis: return False
        return False if len(stack) else True
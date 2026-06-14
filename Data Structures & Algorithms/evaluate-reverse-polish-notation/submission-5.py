class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # convert str to int
            # if tokens, add to stack
            # if tokens are any of '+', '-', '*', and '/', pop last 2 elements
            # Check if empty

            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                last_el = stack.pop()
                second_to_last_el = stack.pop()
                if token == '+':
                    result = second_to_last_el + last_el
                elif token == '-':
                    result = second_to_last_el - last_el
                elif token == '*':
                    result = second_to_last_el * last_el
                elif token == '/':
                    result = int(second_to_last_el / last_el)
                stack.append(result)
        return stack.pop()

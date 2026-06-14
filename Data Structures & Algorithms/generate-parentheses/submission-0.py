from itertools import combinations
from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        comb = combinations(range(n*2), n)
        valid_parantheses = []
        for indices in list(comb):
            stack=deque()
            print(indices)
            combo=""
            for i in range(n*2): 
                if i in indices: 
                    stack.append('(')
                    combo+='('
                else: 
                    if len(stack)==0: break
                    last_paranthesis=stack.pop()
                    combo+=")"
            #print(combo)
            if len(combo)==n*2: valid_parantheses.append(combo) 
        return valid_parantheses
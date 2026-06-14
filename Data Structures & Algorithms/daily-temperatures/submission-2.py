class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """answer=[]
        for i in range(len(temperatures)):
            counter=0
            next_pointer=i
            found_warm=False
            while (next_pointer<=len(temperatures)-1):
                if temperatures[next_pointer]>temperatures[i]: 
                    found_warm=True
                    break
                counter+=1
                next_pointer+=1
            counter = counter if found_warm else 0
            answer.append(counter)
        return answer"""
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
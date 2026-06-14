class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[]
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
        return answer
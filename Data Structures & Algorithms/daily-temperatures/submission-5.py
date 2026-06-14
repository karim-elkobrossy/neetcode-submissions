class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        len_temp = len(temperatures)
        warm_lst = []
        for i in range(len_temp):
            temp_i = temperatures[i]
            found_warmer = False
            for j in range(i+1, len_temp):
                if temperatures[j] > temp_i: 
                    found_warmer = True
                    break
            # Finished looping without finding a warmer day
            if not found_warmer: days_till_warm = 0
            # Found warmer day
            else: days_till_warm = j-i
            warm_lst.append(days_till_warm)  
        return warm_lst           
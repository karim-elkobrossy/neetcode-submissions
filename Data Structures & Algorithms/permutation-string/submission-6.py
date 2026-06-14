class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        for i in range(len_s2):
            # Check permutation on a sliding window
            substring_s2 = s2[i:len_s1+i]
            print(substring_s2)
            if sorted(s1) == sorted(substring_s2): return True
        return False

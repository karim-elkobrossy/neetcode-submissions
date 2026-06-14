import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for x in range(1, sum(piles)-1):
            hours = sum([math.ceil(el/x) for el in piles])
            print(x, hours)
            if hours<=h: return x
        return False
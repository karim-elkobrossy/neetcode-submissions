class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i1, el1 in enumerate(numbers, 1):
            for i2, el2 in enumerate(numbers, 1):
                if i1==i2: continue
                if el1+el2==target: return [i1, i2]
            

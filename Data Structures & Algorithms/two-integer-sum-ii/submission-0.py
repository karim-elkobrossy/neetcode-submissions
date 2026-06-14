class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start<end:
            smaller = numbers[start]
            larger = numbers[end]
            if smaller+larger > target: end-=1
            elif smaller+larger < target: start+=1
            else: return start+1, end+1
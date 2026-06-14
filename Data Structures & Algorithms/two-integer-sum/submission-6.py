class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dct = {}
        for i, el in enumerate(nums):
            remaining_el = target-el
            if remaining_el in seen_dct: return [seen_dct[remaining_el], i]
            seen_dct[el]=i
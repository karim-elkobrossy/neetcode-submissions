class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, el in enumerate(nums):
            remaining_el = target-el
            if remaining_el in nums[i+1:]:
                print(i, remaining_el) 
                return [i, nums.index(remaining_el, i+1)]
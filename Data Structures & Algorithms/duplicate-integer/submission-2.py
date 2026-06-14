class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums))==len(nums)

"""
This avoids using a set, so extra memory is constant, 
but the trade-off is that time complexity goes up from O(n) to O(n log n) due to sorting.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # sort the list in-place
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False"""
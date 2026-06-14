class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder_sum = target-nums[i]
            if remainder_sum in nums:
                remainder_index = nums.index(remainder_sum)
                if i!=remainder_index: return  sorted([i, remainder_index]) 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if len(nums) == 1: return nums[0]
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] > nums[r]: l = mid+1
            else: r = mid
        print(l, mid, r)    
        return nums[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end= 0, len(nums)-1
        if len(nums)<2: return nums[0]
        while start<=end:
            mid = (start+end)//2
            print(start, end, mid)
            if nums[mid]<nums[mid-1]: return nums[mid]
            if nums[mid]<nums[end]: end=mid-1
            else: start=mid+1
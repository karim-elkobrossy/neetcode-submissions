class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        start, end = 0, len(nums)-1
        if len(nums)==0: return -1
        elif len(nums)==1: return 0 if target in nums else -1
        while start<=end:
            mid = (start+end)//2
            print(start, mid, end)
            if nums[mid]==target: return mid
            # From mid to end is sorted if this condition is true
            if nums[mid]<nums[end]: 
                # target is between them (100% it will be between mid to end)
                if nums[mid]<=target<=nums[end]: start=mid+1
                # Target must be on left side (if any)
                else: end=mid-1
            # If mid to end is not sorted then check if target is less than or greater than the end
            else:
                if nums[start]<=target<=nums[mid]: end=mid-1
                else: start=mid+1
        return -1
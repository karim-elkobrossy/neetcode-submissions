class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1: return len(nums)
        nums = sorted(nums)
        print(nums)
        count=0
        max_consec=0
        for i in range(1, len(nums)):
            print(i, nums[i-1], nums[i], count, max_consec, abs(nums[i]-nums[i-1]))
            diff=abs(nums[i]-nums[i-1])
            if diff>1: 
                if max_consec<=count: max_consec=count+1
                count=0
                continue
            elif diff==0: continue
            count+=1
    
        return max(count+1, max_consec)
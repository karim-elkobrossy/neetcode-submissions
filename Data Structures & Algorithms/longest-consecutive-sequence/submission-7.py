class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Initialize variables to track the longest streak
        longest_streak = 1
        current_streak = 1
        
        # Step 3: Traverse the sorted array
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            elif nums[i] == nums[i - 1] + 1:
                current_streak += 1  # Increment the streak
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1  # Reset the streak
        
        # Final check to ensure we account for the last streak
        longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
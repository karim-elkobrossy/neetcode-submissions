class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:  # If the string is empty, return 0
            return 0
        
        char_set = set()  # This set will hold the characters in the current window (substring)
        l = 0  # Left pointer of the window
        max_substring = 0  # Variable to track the maximum length of the substring
        
        # Iterate over the string with the right pointer `r`
        for r in range(len(s)):
            # If the character at s[r] is already in the window (set), we have a duplicate
            while s[r] in char_set:
                # Remove the character at s[l] (move the left pointer) to shrink the window
                char_set.remove(s[l])
                l += 1  # Move left pointer to the right
            
            # Add the current character at s[r] to the set
            char_set.add(s[r])
            
            # Calculate the current window size and update the maximum length
            max_substring = max(max_substring, len(char_set))
        
        return max_substring
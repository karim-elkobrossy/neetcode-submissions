class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1: return len(s)
        visited=set()
        l, r = 0, 1
        visited.add(s[l])
        longest = float("-inf")
        while r<len(s):
            print(visited)
            if s[r] in visited:   
                visited.remove(s[l])
                l+=1
                longest=max(longest, r-l)
                continue        
            else:
                longest=max(longest, r-l)
            print(l, r, longest)
            visited.add(s[r])
            r+=1
        return longest+1

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set(string.ascii_lowercase + string.digits)
        start, end = 0, len(s)-1
        skip = False
        while start<end:
            if s[start].lower() not in alphanumeric:
                start+=1
                continue
            if s[end].lower() not in alphanumeric:
                end-=1
                continue
            if s[start].lower()!=s[end].lower(): return False
            start+=1
            end-=1
        return True
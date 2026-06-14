from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Join lengths without trailing comma
        lengths = ','.join(str(len(word)) for word in strs)
        return lengths + '#' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        lengths_part, string_part = s.split('#', 1)
        # Remove any empty strings that might appear after split
        lengths = list(map(int, filter(None, lengths_part.split(','))))
        
        original_strs = []
        i = 0
        for length in lengths:
            original_strs.append(string_part[i:i+length])
            i += length
        return original_strs
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size=len(s1)
        frequency={}
        #hashmap for frequency of characters (we will later check this condition in a sliding window)
        for c in s1: frequency[c] = frequency.get(c, 0) + 1

        for i in range(len(s2)):
            temp_freq={}
            window_chars=s2[i:i+window_size]
            # Calculate frequency of each character in that window
            for c in window_chars:temp_freq[c]=temp_freq.get(c, 0)+1
            #Check if this frequency dictionary is equal to that of the other dictionary
            conditions=[]
            for c in window_chars:
                if c not in frequency: 
                    # If any of the characters are not in the main word (s1) then make it False
                    conditions.append(False)
                    break
                else: conditions.append(temp_freq[c]==frequency[c])
            if len(conditions)==window_size and all(conditions): return True
        return False
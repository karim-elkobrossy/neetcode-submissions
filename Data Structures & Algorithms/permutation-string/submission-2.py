class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size=len(s1)
        frequency={}
        #hashmap for frequency of characters (we will later check this condition in a sliding window)
        for c in s1: frequency[c] = frequency.get(c, 0) + 1
        print(frequency)
        print('================')

        for i in range(len(s2)):
            temp_freq={}
            window_chars=s2[i:i+window_size]
            print(window_chars)
            for c in window_chars:temp_freq[c]=temp_freq.get(c, 0)+1
            print(i, temp_freq)
            print('=============')
            #Check if this frequency dictionary is within the range of the other dictionary
            conditions=[]
            for c in window_chars:
                print(c, )
                if c not in frequency: 
                    conditions.append(False)
                    break
                else: conditions.append(temp_freq[c]==frequency[c])
            print(conditions)
            if len(conditions)==window_size and all(conditions): return True
        return False
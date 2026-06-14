class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """freq = {}
        print(nums)
        for el in nums:
            freq[i] = freq.get(i,0) + 1
        sorted_freq = [item[0] for item in sorted(freq.items(), key=lambda item: item[1], reverse=True)]
        return sorted_freq[:k]"""
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        print(freq)
        print(sorted(freq, reverse=True))
        return sorted(freq,key=freq.get, reverse=True)[:k]

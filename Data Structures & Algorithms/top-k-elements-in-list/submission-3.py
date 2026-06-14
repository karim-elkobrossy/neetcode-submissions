from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dct = dict(Counter(nums))
        sorted_freq = sorted(freq_dct, key=lambda x: freq_dct[x], reverse=True)
        return sorted_freq[:k]
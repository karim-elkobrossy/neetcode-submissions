from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dct = dict(Counter(nums))
        sorted_freq = sorted(freq_dct, key=freq_dct.get, reverse=True)
        return sorted_freq[:k]
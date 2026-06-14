class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        print(nums)
        for el in nums:
            if el not in freq: freq[el]=1
            else: freq[el]+=1

        sorted_freq = [item[0] for item in sorted(freq.items(), key=lambda item: item[1], reverse=True)]
        return sorted_freq[:k]

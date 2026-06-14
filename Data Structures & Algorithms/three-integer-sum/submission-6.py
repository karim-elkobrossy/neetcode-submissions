class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        for i, el1 in enumerate(nums):
            seen = set()
            for j, el2 in enumerate(nums):
                if i==j: continue
                missing_number = 0-el1-el2
                if missing_number in seen: res_set.add(tuple(sorted((el1, el2, missing_number))))
                else: seen.add(el2)
        return list(res_set)
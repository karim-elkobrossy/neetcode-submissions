class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
    def add(self, val: int) -> int:
        self.nums.append(val)
        print(sorted(self.nums, reverse=True))
        return sorted(self.nums, reverse=True)[self.k-1]

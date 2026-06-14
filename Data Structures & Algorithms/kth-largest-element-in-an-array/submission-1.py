import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sub_array = nums[:k]
        heapq.heapify(sub_array)
        for num in nums[k:]:
            min_subarray = sub_array[0]
            if num > min_subarray:
                heapq.heappop(sub_array)
                heapq.heappush(sub_array, num)
        return heapq.heappop(sub_array)

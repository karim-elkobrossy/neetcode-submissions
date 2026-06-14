class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -math.inf
        i, j = 0, len(heights)-1
        while i < j:
            max_area_temp = min(heights[i], heights[j]) * (j-i)
            max_area = max(max_area_temp, max_area)
            if heights[j] > heights[i]: i+=1
            else: j-=1
        return max_area
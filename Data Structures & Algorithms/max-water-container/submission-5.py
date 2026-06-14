class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        maximum = -1
        while start<end:
            area = min(heights[start], heights[end])*(end-start)
            print(heights[start], heights[end], area)
            #print(start, end, area)
            maximum=max(area, maximum)
            if heights[start] < heights[end]: start+=1
            else: end-=1
        return maximum
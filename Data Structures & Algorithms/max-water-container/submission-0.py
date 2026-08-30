class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        maxx = 0
        while p2 > p1:
            if min(heights[p1], heights[p2]) * (p2 - p1) > maxx: 
                maxx = min(heights[p1], heights[p2]) * (p2 - p1)
            if heights[p1] > heights[p2]:
                p2 -= 1
            else: 
                p1 += 1
        return maxx 


        
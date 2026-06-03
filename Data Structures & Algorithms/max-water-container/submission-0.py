class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        # l, r = 0, n-1
        water = 0
        # while l<=r:
        #     lefth = height[l]
        #     righth = height[r]
        #     if lefth<righth:
        #         #leftside is smaller than right side
        #         #
        #     else:

        for l in range(n):
            for r in range(n):
                max_height_container = min(heights[l], heights[r])
                water = max(water, max_height_container*(r-l))

        return water
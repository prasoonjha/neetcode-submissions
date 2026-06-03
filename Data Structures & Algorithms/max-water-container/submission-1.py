class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        water = 0
        #brute force
        # for l in range(n):
        #     for r in range(n):
        #         max_height_container = min(heights[l], heights[r])
        #         water = max(water, max_height_container*(r-l))

        l, r = 0, n-1
        #left pointer, right pointer
        """
        l, r = 0, n-1
        while l<=r:
            left_h
            right_h
            while left_h <=right_h:
                if height[left_h] <right_height
                    left side is smaller, which means that between

        """ 
        max_l = -1
        max_r = -1
        while l<=r:
            lefth = heights[l]
            righth = heights[r]
            if lefth<righth:
                #leftside is smaller than right side
                max_l = max(max_l, lefth)
                water = max(water, max_l*(r-l))
                l+=1
            else:
                max_r = max(max_r, righth)
                water = max(water, max_r*(r-l))
                r-=1
                

        return water
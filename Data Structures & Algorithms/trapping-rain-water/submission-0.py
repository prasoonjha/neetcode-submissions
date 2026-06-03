class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        n = len(height)
        l, r = 0, n-1
        max_l, max_r = 0, 0
       
        while l<=r:
            left_height = height[l]
            right_height = height[r]
            
            if left_height < right_height:

                max_l = max(max_l, left_height)

                trapped += max_l - left_height
                l+=1
            else:

                max_r = max(max_r, right_height)

                trapped += max_r - right_height
                r-=1
                
        return trapped
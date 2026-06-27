class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Why m is incremented after swapping with l
        When nums[m] == 0, everything before l is already guaranteed
        to be 0, so after swapping, the element that comes to position
        m is known to be 1 (or it's the same element when l == m). 
        Therefore, it's safe to move m forward.
        Why m is not incremented after swapping with r?
        When you swap with r, the element brought into position
        m hasn't been processed yet—it could be 0, 1, or 2. 
        So you must examine nums[m] again in the next iteration.
         INVARIANT:
        [0 ... l-1]     -> all 0s
        [l ... m-1]     -> all 1s
        [m ... r]       -> unknown
        [r+1 ... end]   -> all 2s
        """
        n = len(nums)
        l, m, r = 0,0,n-1
        while m<=r:
            if nums[m] == 0:
                #swap with l
                nums[l], nums[m] = nums[m], nums[l]
                #increase l, dont increase m
                l+=1
                m+=1 # safe to move m forward as 
            elif nums[m] == 1:
                #no swap needed
                m+=1
            else:
                #swap with r
                nums[m], nums[r] = nums[r], nums[m]
                r-=1
        

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n-1
        i = 0
        while i<=r:
            if nums[i] == 0:
                #swap with left
                nums[l], nums[i] = nums[i], nums[l]
                #increment left
                l+=1
            if nums[i] == 2:
                #swap with right
                nums[i], nums[r] =  nums[r], nums[i] 
                #decrement right
                r-=1
                i-=1
            i+=1 
            

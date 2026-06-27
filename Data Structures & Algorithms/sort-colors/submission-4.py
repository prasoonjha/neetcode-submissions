class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, m, r = 0,0,n-1
        while m<=r:
            if nums[m] == 0:
                #swap with l
                nums[l], nums[m] = nums[m], nums[l]
                #increase l, dont increase m
                l+=1
                m+=1
            elif nums[m] == 1:
                #no swap needed
                m+=1
            else:
                #swap with r
                nums[m], nums[r] = nums[r], nums[m]
                r-=1
        

class Solution:
    
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        def rotateHelper(l: int, r: int) -> None:
            while l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        
        
        
        rotateHelper(0,n-1)
        rotateHelper(0,k-1)
        rotateHelper(k, n-1)
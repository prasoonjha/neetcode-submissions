class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        k = 0
        while l<=r:
            if nums[l] == val:
                #swap with r
                nums[l], nums[r] = nums[r], nums[l]
                #decrement r
                r-=1
                #decrement l as well to nullify increment
                l-=1
            else:
                k+=1
            l+=1
        return k
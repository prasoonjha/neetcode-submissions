class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i in range(n):
            num = nums[i]
            if nums[abs(num)-1]<0:
                res = abs(num)
                break
            nums[abs(num)-1] *= -1
        return res
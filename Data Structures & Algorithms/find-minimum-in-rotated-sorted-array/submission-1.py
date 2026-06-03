class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = float("inf")
        while l<=r:
            mid = (l+r)//2
            n = nums[mid]
            #left half is sorted
            res = min(res, nums[mid])
            if nums[l]<=nums[mid]:
                #ignore, but before that,
                #take into account the smallest num in sorted part
                res = min(res, nums[l])
                l=mid+1
            else:
                #right half is sorted
                res = min(res, nums[mid])
                r=mid-1

        return res
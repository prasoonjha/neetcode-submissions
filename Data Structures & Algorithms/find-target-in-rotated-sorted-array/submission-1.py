class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            n = nums[mid]
            if n == target:
                return mid
            #now first check which half is sorted
            if nums[l] <= n:
                #left half is sorted
                if nums[l] <= target < n:
                    r=mid-1
                else:
                    l=mid+1
            else:
                #right half is sorted
                if n < target <= nums[r]:
                    l=mid+1
                else:
                    r=mid-1

        return -1
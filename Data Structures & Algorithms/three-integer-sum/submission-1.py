class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #3 nums sum to 0, invariant:sum of 2 must be equal -(3rd),
        """
        iterate through the array.
        at each index i, we need to figure out sum with j such that i!=j
        for each sum, we check if that sum is equal to any
        what should we store in the map?

        """
        res = set()
        n = len(nums)

        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                target = -nums[i] - nums[j]
                if target in seen:
                    res.add(tuple(sorted([nums[i], nums[j], target])))
                #since i is fixed, we keep a track of j, so this is essentially reduced
                #to two sum problem
                seen.add(nums[j])

        return [list(t) for t in res]



"""
O(n^2)
use a hashmap 


O(n^3)
brute force 3 pointer
n = len(nums)
        res = []
        for i in range(n):
            nums_i = nums[i]
            j=n-1
            while j>0:
                if j==i:
                    j-=1
                    continue
                nums_j = nums[j]
                sum_ij = nums_i+nums_j
                k = n-1
                while k>0:
                    if k==j or k==i:
                        k-=1
                        continue
                    else:
                        if sum_ij == -nums[k]:
                            if [nums_i, nums_j, nums[k]] not in res:
                                res.append([nums_i, nums_j, nums[k]])
                    k-=1
                j-=1
        return res
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        curr = []
        def dfs(i, curr):
            if i == n:
                subsets.append(curr)
                return
            #left chlild considering nums[i]
            dfs(i+1, curr+[nums[i]])
            #right child discarding nums[i]
            dfs(i+1, curr)
        dfs(0, curr)
        return subsets
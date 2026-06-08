class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, curr):
            nonlocal res
            if i==n:
                res.append(curr)
                return
            dfs(i+1, curr+[nums[i]])
            dfs(i+1, curr)
        dfs(0, [])
        return res
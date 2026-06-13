class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(remaining, i, curr):
            if len(remaining) == 0:
                res.append(curr)
                return
            for j in range(len(remaining)):
                dfs(remaining[:j]+remaining[j+1:], j+1,curr+[remaining[j]])
        dfs(nums, 0, [])
        return res
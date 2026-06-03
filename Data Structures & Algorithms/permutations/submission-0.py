class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def dfs(remaining, curr):
            if len(remaining) == 0:
                res.append(curr)
                return
            for i in range(len(remaining)):
                dfs(remaining[:i]+remaining[i+1:], curr+[remaining[i]])
        dfs(nums, [])
        return res
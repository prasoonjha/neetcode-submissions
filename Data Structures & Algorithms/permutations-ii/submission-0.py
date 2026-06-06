class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        def dfs(remaining, curr):
            if not remaining:
                res.append(curr)
                return
            for i in range(len(remaining)):
                if i>0 and remaining[i]==remaining[i-1]:
                    continue
                dfs(remaining[:i]+remaining[i+1:], curr+[remaining[i]])
        dfs(nums, [])
        return res
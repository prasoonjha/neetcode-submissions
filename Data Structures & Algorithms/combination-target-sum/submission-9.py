class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, curr, remaining):
            nonlocal res
            if remaining == 0:
                res.append(curr)
                return 
            for j in range(i,n):
                if remaining>=nums[j]:
                    dfs(j, curr+[nums[j]], remaining-nums[j])
        dfs(0, [], target)
        return res
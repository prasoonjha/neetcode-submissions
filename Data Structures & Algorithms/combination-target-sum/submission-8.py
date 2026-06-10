class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, remaining, curr):
            if remaining == 0:
                res.append(curr)
                return
            for start in range(i,n):
                if remaining>=nums[start]:
                    dfs(start, remaining-nums[start], curr+[nums[start]])
        dfs(0, target, [])
        return res
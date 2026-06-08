class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, remaining, curr):
            if remaining == 0:
                res.append(curr)
            for j in range(i, n):
                if remaining<nums[j]:
                    continue
                dfs(j, remaining-nums[j], curr+[nums[j]])
        dfs(0, target, [])
        return res
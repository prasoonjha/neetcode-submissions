class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(start, remaining, curr):
            if remaining == 0:
                res.append(curr)
                return
            
            for i in range(start, n):
                if nums[i]>remaining:
                    continue
                dfs(i, remaining-nums[i], curr+[nums[i]])

        dfs(0, target, [])

        return res
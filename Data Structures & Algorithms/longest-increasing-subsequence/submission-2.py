class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def dfs(i):
            if i in cache: return cache[i]
            if i == n:
                return 0
            max_len = 1
            for j in range(0, i):
                if nums[j] <nums[i]:
                    max_len = max(max_len, 1+dfs(j))
            cache[i] = max_len
            return max_len
        return max(dfs(i) for i in range(n))
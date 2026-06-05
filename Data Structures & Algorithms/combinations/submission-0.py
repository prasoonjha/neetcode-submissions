class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, curr):
            if i == n+1:
                if len(curr) == k:
                    res.append(curr)
                return
            dfs(i+1, curr+[i])
            dfs(i+1, curr)
        dfs(1, [])
        return res
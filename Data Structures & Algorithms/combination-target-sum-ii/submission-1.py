class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(start, remaining, curr):
            if remaining == 0:
                res.append(curr.copy())
                return
            for i in range(start,n):
                if remaining<candidates[i] or (i>start and candidates[i]==candidates[i-1]):
                    continue
                dfs(i+1, remaining-candidates[i], curr+[candidates[i]])
        dfs(0, target, [])
        return res
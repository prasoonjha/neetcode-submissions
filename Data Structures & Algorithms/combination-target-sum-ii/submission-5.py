class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def dfs(i, curr, remaining):
            nonlocal res
            if remaining == 0:
                res.append(curr)
                return 
            for j in range(i,n):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if remaining>=candidates[j]:
                    dfs(j+1, curr+[candidates[j]], remaining-candidates[j])
        dfs(0, [], target)
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        def dfs(start,curr, remaining):

            if remaining == 0:
                res.append(curr.copy())
                return
            for i in range(start, n):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]<=remaining:
                    dfs(i+1, curr+[candidates[i]], remaining-candidates[i])
        dfs(0, [], target)
        return res

        
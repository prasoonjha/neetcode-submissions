class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        def dfs(i, remaining, curr):
            if remaining == 0:
                res.append(curr)
            for start in range(i,n):
                if start>i and candidates[start]==candidates[start-1]:
                    continue
                if remaining>=candidates[start]:
                    dfs(start+1, remaining-candidates[start], curr+[candidates[start]])
        dfs(0, target, [])
        return res

        
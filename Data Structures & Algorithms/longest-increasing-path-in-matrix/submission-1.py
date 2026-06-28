class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}

        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            if r<0 or r==ROWS or c<0 or c==COLS:
                return 0
            ans = 1
            for dr, dc in [(0,1), (1,0), (-1, 0), (0, -1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<ROWS and 0<=nc<COLS and matrix[nr][nc]>matrix[r][c]:
                    ans = max(ans, 1+dfs(nr, nc))
                cache[(r,c)] = ans
            return ans
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))

        return res
        
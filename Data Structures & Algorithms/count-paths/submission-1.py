class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        cache={}
        def dfs(r,c):
            if r<0 or r==m or c<0 or c==n:
                return 0
            if r==m-1 and c==n-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]
            res=dfs(r+1,c)+dfs(r,c+1)
            cache[(r,c)]=res
            return res
        return dfs(0,0)

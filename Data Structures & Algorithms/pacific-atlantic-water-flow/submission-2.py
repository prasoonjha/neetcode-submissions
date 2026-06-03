class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac_reachable = set()
        atl_reachable = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r, c, visited):
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visited:
                return
            visited.add((r,c))
            for direction in directions:
                dr, dc = direction
                nr, nc = r+dr, c+dc
                if 0<=nr<ROWS and 0<=nc<COLS and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for c in range(COLS):
            dfs(0,c, pac_reachable)
            dfs(ROWS-1, c, atl_reachable)
        for r in range(ROWS):
            dfs(r,0, pac_reachable)
            dfs(r, COLS-1, atl_reachable)

        return [list(t) for t in pac_reachable.intersection(atl_reachable)]
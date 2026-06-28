class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(source):
            q = deque([source])
            while q:
                r,c = q.popleft()
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr, nc = r+dr,c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"
                      
        res = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    print("new island")
                    bfs((r,c))
                    res+=1

        return res
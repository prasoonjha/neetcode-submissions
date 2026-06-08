class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        WATER = -1
        TREASURE = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque([])
        #append (r,c) into queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for direction in directions:
                dx, dy = direction
                nr, nc = dx+r, dy+c
                if (0<=nr<ROWS) and (0<=nc<COLS) and (grid[nr][nc] == INF):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))


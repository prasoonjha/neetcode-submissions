class Solution:
    

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        WATER = -1
        TREASURE = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        q = deque([])
        # add sources to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        #start bfs from each source
        while q:
            n = len(q)
            for _ in range(n):
                source_node = q.popleft()
                r, c = source_node
                for direction in directions:
                    dx, dy = direction
                    nr, nc = r+dx, c+dy
                    #sanity check
                    if (0<=nr<ROWS) and (0<=nc<COLS) and (grid[nr][nc] == INF) and ((nr, nc) not in visited):
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))
                        visited.add((nr,nc))

                    
        

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque([])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        fresh = 0
        #add sources to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                
        #start dfs from each source
        time_elapsed = 0
        while q:
            n = len(q)
            rotted = False
            for _ in range(n):
                node = q.popleft()
                r, c = node

                for direction in directions:
                    dr, dc = direction
                    nr, nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh-=1
                        q.append((nr, nc))
                        rotted = True
            if rotted: time_elapsed +=1
        
        return time_elapsed if fresh == 0 else -1
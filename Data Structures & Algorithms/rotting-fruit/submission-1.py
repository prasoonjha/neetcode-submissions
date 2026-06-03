from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minutes_elapsed = 0
        q = deque([])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        
        #add all rotten fruits in queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh+=1

        while q and fresh>0:           
            for _ in range(len(q)):
                r, c = q.popleft()
                for direction in directions:
                    dx, dy = direction
                    nr, nc = r+dx, c+dy
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh-=1
            minutes_elapsed+=1
                   
        if fresh>0:
            return -1
        return minutes_elapsed
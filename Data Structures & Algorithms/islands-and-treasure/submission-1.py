from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque([])
        directions = [(0, 1),(0, -1), (-1, 0), (1, 0)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            r, c = q.popleft()
            for direction in directions:
                dx, dy = direction
                if 0<=r+dx<ROWS and 0<=c+dy<COLS and grid[r+dx][c+dy] == INF:
                    grid[r+dx][c+dy] = grid[r][c]+1
                    q.append((r+dx, c+dy))
                



        # def dfs(r, c, distance):
        #     if r<0 or c<0 or r>=ROWS or c>=COLS:
        #         return
        #     if grid[r][c] < distance:
        #         return
        #     grid[r][c] = distance
        #     dfs(r+1,c,distance+1)
        #     dfs(r-1,c,distance+1)
        #     dfs(r,c+1,distance+1)
        #     dfs(r,c-1,distance+1)
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 0 :
        #             dfs(r, c, 0)
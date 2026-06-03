class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited =  set()

        def dfs(r, c):
            if (r, c) in visited:
                #in case already visited 0 contribution to perimeter
                return 0
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c] == 0:
                #if we hit boundary or water, 1 unit of contrubution to perimeter
                return 1
            #mark visited
            visited.add((r, c))
                
            #add contributions from surrounding cells
            return dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1)
            

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1:
                    #in case first land is found, start dfs and return parameter
                    return dfs(r, c)
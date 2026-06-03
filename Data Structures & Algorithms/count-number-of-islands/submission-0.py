class Solution:
    

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        numIslands = 0
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col):
            if row<0 or col<0 or col>=COLS or row>=ROWS or grid[row][col] == '0' or visited[row][col]:
                return
            
            visited[row][col] = 1

            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row, col-1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and not visited[r][c]:
                    numIslands += 1
                    dfs(r,c)

        return numIslands
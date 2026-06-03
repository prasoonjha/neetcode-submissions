class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        result = []

        def dfs(r, c, visited):
            # mark visited immediately
            visited.add((r, c))

            # check if this cell touches either ocean
            pacific = (r == 0 or c == 0)
            atlantic = (r == ROWS - 1 or c == COLS - 1)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visited and
                    heights[nr][nc] <= heights[r][c]
                ):
                    p, a = dfs(nr, nc, visited)
                    pacific = pacific or p
                    atlantic = atlantic or a

            return pacific, atlantic

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                p, a = dfs(r, c, visited)
                if p and a:
                    result.append([r, c])

        return result

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        spiral = []
        def helper(top, right, bottom, left):
            if top>bottom or left>right:
                return
            #print top row 
            for c in range(left, right+1):
                spiral.append(matrix[top][c])
                
            #print right col
            for r in range(top+1, bottom+1):
                spiral.append(matrix[r][right])
                
            
            #print bottom row if top<bottom
            if top<bottom:
                for c in range(right-1, left-1, -1):
                    spiral.append(matrix[bottom][c])
                
            #print left col if left<right
            if left<right:
                for r in range(bottom-1, top, -1):
                    spiral.append(matrix[r][left])

            #print inner matrix
            helper(top+1,right-1, bottom-1, left+1)
        helper(0, COLS-1, ROWS-1, 0)
        return spiral
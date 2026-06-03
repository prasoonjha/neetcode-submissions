class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r, c = 0, cols-1
        while 0<=r<rows and 0<=c<cols:
            curr_num = matrix[r][c]
            if curr_num==target:
                return True
            if curr_num>target:
                c-=1
            else:
                r+=1
        return False
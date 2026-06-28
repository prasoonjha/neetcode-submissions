class Solution:
    def transpose(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            for c in range(n):
                if r>c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                else:
                    continue

    def flip(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            row.reverse()

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.flip(matrix)
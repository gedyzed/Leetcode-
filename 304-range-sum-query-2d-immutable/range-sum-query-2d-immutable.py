class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.mat = matrix
        n, m = len(self.mat), len(self.mat[0])
        for r in range(n):
            for c  in range(m):

                up = self.mat[r][c - 1] if c > 0 else 0
                left = self.mat[r - 1][c] if r > 0 else 0
                diag = self.mat[r - 1][c - 1] if r > 0 and c > 0 else 0

                self.mat[r][c] += up + left - diag

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        up = self.mat[row1 - 1][col2] if row1 > 0 else 0
        left = self.mat[row2][col1 - 1] if col1 > 0 else 0
        diag = self.mat[row1 - 1][col1 - 1] if col1 > 0 and row1 > 0 else 0

        return self.mat[row2][col2] - up - left + diag
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
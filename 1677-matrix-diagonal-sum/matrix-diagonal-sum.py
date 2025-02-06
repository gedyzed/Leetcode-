class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if not (row - col) or row + col == len(mat[0]) - 1:
                    sum += mat[row][col]
        return sum            

        
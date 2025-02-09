class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if col > row:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(len(matrix)):
            matrix[row].reverse()
            

                

        
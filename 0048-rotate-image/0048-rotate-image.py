class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix) # row
        n=len(matrix[0]) # column

        # reverse each column from right to left
        left = 0 
        right = m-1 
        while left < right:
            matrix[left],matrix[right] = matrix[right],matrix[left] # swapping the first and the last index
            left += 1
            right -= 1

        # Transpose the reverse matrix
        for i in range(m):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

     
        
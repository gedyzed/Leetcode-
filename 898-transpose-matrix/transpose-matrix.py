class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        mat = []
        for col in range(len(matrix[0])):
            result = []
            for row in range(len(matrix)):
                result.append(matrix[row][col])
            mat.append(result)  

        return mat      

        
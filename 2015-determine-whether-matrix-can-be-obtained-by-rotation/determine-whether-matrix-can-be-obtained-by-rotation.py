class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def transpose(mat):
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    if col >= row:
                        mat[row][col], mat[col][row] = mat[col][row], mat[row][col]

        for _ in range(3):
            if mat == target:
                return True
            transpose(mat)
            mat.reverse()
            if mat == target:
                return True
        return False            


                           
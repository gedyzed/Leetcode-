class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                num = triangle[i][j]
                triangle[i][j] = num +  min(triangle[i + 1][j + 1], triangle[i + 1][j])

        return triangle[0][0]


        
            


        
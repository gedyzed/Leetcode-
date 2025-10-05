class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        dp = [[0] * (i + 1) for i in range(m)]
        for j in range(m):
            dp[-1][j] = triangle[-1][j]
       
        for i in range(m - 2, -1, -1):
            for j in range(i + 1):
                num = triangle[i][j]
                dp[i][j] = num +  min(dp[i + 1][j + 1], dp[i + 1][j])

        return dp[0][0]


        
            


        
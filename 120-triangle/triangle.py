class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        dp, max_ = [], 0
        for i in range(m):
            n = len(triangle[i]) + 1
            dp.append([0] * n)
            max_ = max(max_, n)
        
        dp.append([0] * max_)
        for i in range(m - 1, -1, -1):
            n = len(triangle[i])
            for j in range(n - 1, -1, -1):
                num = triangle[i][j]
                dp[i][j] = num +  min(dp[i + 1][j + 1], dp[i + 1][j])

        return dp[0][0]


        
            


        
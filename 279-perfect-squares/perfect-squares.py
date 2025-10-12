class Solution:
    def numSquares(self, n: int) -> int:

        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [float("inf")] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for square in squares:
                sum = i - square 
                if sum >= 0:
                    dp[i] = min(dp[i], 1 + dp[sum])
           
        return dp[n] - 1
                 
                 
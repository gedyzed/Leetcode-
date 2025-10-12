class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float("inf")] * (n + 1)
        dp[n] = 1
        for i in range(n, -1, -1):
            num = 1
            while num * num <= n:
                sum = i + num * num
                if sum <= n:
                    dp[i] = min(dp[i], 1 + dp[sum])
                num += 1

        return dp[0] - 1
                 
           

            






            

      
        

        
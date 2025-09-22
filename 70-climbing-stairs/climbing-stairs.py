class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = defaultdict(int)
        def dp(i):

            if i in memo:
                return memo[i]
            if i < 3:
                return i

            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)



       
        
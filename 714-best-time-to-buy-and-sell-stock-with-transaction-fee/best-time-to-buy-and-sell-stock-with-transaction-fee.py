class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        memo = defaultdict(int)
        def dp(idx, buy):
            index = (idx, buy)
            if index in memo:
                return memo[index]

            if idx == len(prices):
                return 0
           
            if buy:
                profit = max(
                    -prices[idx] + dp(idx + 1, 0), 
                    dp(idx + 1, 1)
                    )
            else:
                profit = max(
                    prices[idx] - fee + dp(idx + 1, 1), 
                    dp(idx + 1, 0)
                    )
                    
            memo[index] = profit
            return profit

        return dp(0, 1)
            



       





        
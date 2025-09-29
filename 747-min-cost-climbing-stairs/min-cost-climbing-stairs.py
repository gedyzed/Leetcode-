class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = defaultdict(int)
        def dp(idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(cost):
                return 0
        
            cost_ = min(dp(idx + 1) + cost[idx], dp(idx + 2) + cost[idx])
            memo[idx] = cost_
            return cost_
    
        return min(dp(0) , dp(1))
            





        
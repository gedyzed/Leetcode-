class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo = defaultdict(int)
        def dp(left, right):

            idx = (left, right)
            if idx in memo:
                return memo[idx]

            if left == right:
                return 0
            
            res = max(piles[left], piles[right]) + max(dp(left + 1, right), dp(left, right - 1))
            memo[idx] = res
            return res

        sum_ = dp(0, len(piles) - 1)
        return sum_ > sum(piles) // 2
        

        
        
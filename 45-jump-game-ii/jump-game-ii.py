class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0
        for idx in range(n - 2, -1, -1):
            for step in range(1, nums[idx] + 1):
                next_idx = step + idx
                if next_idx >= (n - 1):
                    dp[idx] = 1
                    break
                else:
                    dp[idx] = min(dp[idx], 1 + dp[next_idx])

    
        return dp[0]

       

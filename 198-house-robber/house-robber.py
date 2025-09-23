class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = defaultdict(int)
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == 0:
                return nums[0]
            
            if i == 1:
                return max(nums[0], nums[1])

            memo[i] = max(dp(i - 1),  dp(i - 2) + nums[i])
            return memo[i]
        
        return dp(len(nums) - 1)



        
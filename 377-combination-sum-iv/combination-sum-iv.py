class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            if rem in memo:
                return memo[rem]
            
            count = 0
            for n in nums:
                count += dp(rem - n)
            
            memo[rem] = count
            return count

        return dp(target)

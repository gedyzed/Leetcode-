class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = defaultdict(int)
        def dp(index, curr_sum):

            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            if index == len(nums) and curr_sum == target:
                return 1
            if index == len(nums) and curr_sum != target:
                return 0  

            count = dp(index + 1, curr_sum +  nums[index])
            count += dp(index + 1, curr_sum - nums[index])
            memo[(index, curr_sum)] = count
            return count
        return dp(0, 0)
        
        
            
            





        
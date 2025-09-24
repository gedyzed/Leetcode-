class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # def backtrack(index, currentSum):
        #     count = 0
        #     if index >= len(nums):
        #         if currentSum == target:
        #             count += 1
        #         return count
            
        #     count += backtrack(index + 1, currentSum + nums[index])
        #     count += backtrack(index + 1, currentSum - nums[index])

        #     return count
        # return backtrack(0, 0)

        memo = defaultdict(int)
        def dp(index, prevail):

            if (index, prevail) in memo:
                return memo[(index, prevail)]
            
            if index == len(nums) and not prevail:
                return 1
            if index == len(nums) and prevail:
                return 0  

            count = dp(index + 1, prevail - nums[index])
            count += dp(index + 1, prevail + nums[index])
            memo[(index, prevail)] = count
            return count
        return dp(0, target)
        
        
            
            





        
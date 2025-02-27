class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        # find the max_sum
        presum = 0
        max_sum = float('-inf')
        for right in range(len(nums)):
            if presum < 0:
                presum = 0
            presum += nums[right]
            max_sum = max(max_sum, presum)
        
        # find the min_sum
        presum = 0
        min_sum = float('inf')
        for right in range(len(nums)):
            if presum > 0:
                presum = 0
            presum += nums[right] 
            min_sum = min(min_sum, presum)   

        # return the max of the two abs
        return max(max_sum, abs(min_sum))    










   
        
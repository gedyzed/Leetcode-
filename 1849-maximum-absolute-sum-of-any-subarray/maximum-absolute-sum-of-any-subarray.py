class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        
        presum = 0
        max_sum = float('-inf')
        for right in range(len(nums)):
            if presum < 0:
                presum = 0
            presum += nums[right]
            max_sum = max(max_sum, presum)
        
        presum = 0
        min_sum = float('inf')
        for right in range(len(nums)):
            if presum > 0:
                presum = 0
            presum += nums[right] 
            min_sum = min(min_sum, presum)   

        return max(max_sum, abs(min_sum))    










   
        
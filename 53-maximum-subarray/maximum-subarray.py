class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float('-inf')
        presum = 0
        for num in nums:
            presum += num
            max_sum = max(max_sum, presum)
            if presum < 0:
                presum = 0

        return max_sum         
        
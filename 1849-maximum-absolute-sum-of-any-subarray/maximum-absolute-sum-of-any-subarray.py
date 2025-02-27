class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        return max(presum) - min(presum)    
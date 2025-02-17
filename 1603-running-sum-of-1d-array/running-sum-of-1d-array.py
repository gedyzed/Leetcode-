class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        prefix = 0
        for i in range(len(nums)):
            nums[i] = prefix + nums[i]
            prefix = nums[i]

        return nums     
        
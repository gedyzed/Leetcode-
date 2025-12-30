class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = max_ = 0
        for i in range(len(nums)):
            if not count and nums[i]:
                count = 1
            elif i > 0 and nums[i - 1] and nums[i]:
                count += 1
            elif not nums[i]:
                count = 0

            max_ = max(count, max_)
            
        return max_
            
        
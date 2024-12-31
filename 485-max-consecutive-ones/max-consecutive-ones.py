class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        left = max_ = 0
        for right in range(len(nums)):
            if not nums[right]:
                left = right + 1
            max_ =  max(max_, right - left + 1)  
            
        return max_     
        
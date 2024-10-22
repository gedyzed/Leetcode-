class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        i = 0
        while i < len(nums) :
            if nums[i] != i + 1:
                return i+1
            i += 1    
        return i+1        





        
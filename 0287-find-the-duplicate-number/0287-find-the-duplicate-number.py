class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[correct] == nums[i] and correct != i:
                return nums[i]
            elif nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]  
            else:
                i += 1
                
        return -1           
        
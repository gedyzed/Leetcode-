class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):
            if nums[i] != (i + 1) and nums[nums[i] - 1] != nums[i]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return [nums[i], i + 1]
      
   
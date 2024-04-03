class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        left= 0

        for right in range(1,len(nums)):
            if nums[right] == nums[left]:
                nums[left] *= 2
                nums[right] = 0
                left += 1
            else:
                left += 1
              
        left = 0
        for right in range(len(nums)):
           if nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1

        return nums               
        
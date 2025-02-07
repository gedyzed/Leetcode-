class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *=  2  
                nums[i] = 0

        left = 0 
        right = 1

        while right < len(nums):
            if nums[right] and not nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left]:
                left += 1  
                    
            right += 1

        return nums    
               

                



       

        
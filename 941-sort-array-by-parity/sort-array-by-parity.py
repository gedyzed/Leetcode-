class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        left = 0
        for right in range(len(nums)):
            if left != right and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]   
                left += 1
                
            if nums[left] % 2 == 0:
                left += 1


        return nums          
       
        
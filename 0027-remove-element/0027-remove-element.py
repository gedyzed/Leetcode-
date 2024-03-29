class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            if nums[left]== val:
                nums.remove(val)
                right -= 1
            elif nums[right] == val:
                nums.remove(val)
                right -= 1
            else:
                right -= 1
                left += 1
    
        return len(nums)        
                
                
        
        
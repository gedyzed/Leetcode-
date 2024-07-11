class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        left,counter = 0,0

        

        for right in range(len(nums)):
            if not nums[right]:
                counter += 1 
         
            while counter > 1:      
                if nums[left] == 0: 
                    counter -= 1 
                left += 1    
                
            max_length = max(max_length,right-left)      
            
        return max_length           




        
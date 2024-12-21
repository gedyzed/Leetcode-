class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        current_length = 0
        
        for i in range(len(nums)):
        
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                current_length = 1  
                
                for j in range(i + 1, len(nums)):
                    if nums[j] <= threshold and nums[j] % 2 != nums[j - 1] % 2:
                        current_length += 1
                    else:
                        break
                
                max_length = max(max_length, current_length)
        
        return max_length

        

        
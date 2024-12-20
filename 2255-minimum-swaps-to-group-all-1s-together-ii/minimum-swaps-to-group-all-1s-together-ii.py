class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        windowLength = sum(nums)
        currentZeros = min_swaps = windowLength - sum(nums[:windowLength]) 

        for left in range(len(nums)):
            
            right = (left + windowLength) % len(nums) 
            if not nums[right]:
                currentZeros += 1      
     
            if not nums[left] :
                currentZeros -= 1
            min_swaps = min(min_swaps, currentZeros)  

        return min_swaps          


    
        
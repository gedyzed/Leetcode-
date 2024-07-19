class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minSize = 100001 # since the maximum size is 10^5
        targetsum = 0
        left = 0

        for right in range(len(nums)):
            targetsum += nums[right]
            while targetsum >= target :
                minSize = min(minSize,right - left + 1) 
                targetsum -= nums[left]  
                left += 1 

        if minSize == 100001:
            minSize = 0
            
        return minSize        

        
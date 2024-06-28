class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxAverage = -999999
        currentAverage = 0
        currentSum = 0

        for index in range(len(nums)):
            currentSum += nums[index]
            if index >= k-1:
                maxAverage = max(currentSum/k,maxAverage)
                currentSum -= nums[index-k+1]
        return maxAverage        
                
            

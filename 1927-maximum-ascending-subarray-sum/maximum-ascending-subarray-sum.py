class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        max_sum = sum = nums[0]
        for i in range(1, len(nums)):
            sum = sum + nums[i] if nums[i] > nums[i - 1] else nums[i]
            max_sum = max(max_sum, sum)   

        return max_sum    
                
             
            


            


        
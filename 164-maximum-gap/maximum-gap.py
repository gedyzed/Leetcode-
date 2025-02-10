class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        nums.sort()
        gap = 0 
        for i in range(1, len(nums)):
            gap = max(gap, nums[i] - nums[i - 1])

        return gap    


             

   


        
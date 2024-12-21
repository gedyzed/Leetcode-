class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        min_difference = float('inf')
        for i in range(len(nums)):
            if i >= k - 1:
                min_difference = min(min_difference, nums[i] - nums[i - k + 1])
        return min_difference           


            
              



    
                    
        
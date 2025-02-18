class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(goal):    
            left = count = presum = 0
            for right in range(len(nums)):
                presum += nums[right]

                while presum > goal and left <= right :
                    presum -= nums[left]
                    left += 1

                count += right - left + 1
            
            return count  
              
        return helper(goal) - helper(goal - 1)    
        
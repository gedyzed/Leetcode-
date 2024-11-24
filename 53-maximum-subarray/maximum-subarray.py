class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        total = 0

        for num in nums:
            if total < 0:
                total = 0

            total += num   
            ans = max(ans, total)
        return ans    
      
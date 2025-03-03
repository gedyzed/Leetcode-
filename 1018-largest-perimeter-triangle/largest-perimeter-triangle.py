class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        max_p = left = 0
        sum_ = sum(nums[:2])
        for i in range(2, len(nums)):

            if sum_ > nums[i]:
                max_p = max(max_p, sum_ + nums[i])
                
            sum_ -= nums[left]   
            sum_ += nums[i]
            left += 1

        return max_p        
          
[2, 3, 3, 4]
                
        
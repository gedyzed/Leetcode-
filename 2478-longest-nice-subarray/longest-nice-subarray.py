class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        left, max_len = 0, 1
        temp = nums[0]
        for right in range(1, len(nums)):

            while temp & nums[right] and left <= right:
                temp ^= nums[left]
                left += 1

            if temp & nums[right]  == 0:
                temp |= nums[right]

            max_len = max(max_len, right - left + 1) 

        return max_len 
                




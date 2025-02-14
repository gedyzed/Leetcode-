class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = count = max_len = 0
        for right in range(len(nums)):

            if not nums[right]:
                count += 1

            while count > k:
                if not nums[left]:
                    count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)  

        return max_len              


        
class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        min_sum = float('inf')
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[j] > nums[i] and nums[j] > nums[k]:
                        sum = nums[j] + nums[i] + nums[k]
                        min_sum = min(min_sum, sum)

        return min_sum if min_sum != float('inf') else -1     

        
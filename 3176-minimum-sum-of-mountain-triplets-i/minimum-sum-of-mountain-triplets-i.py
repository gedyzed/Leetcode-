class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        min_sum = float('inf')
        for i in range(1, len(nums) - 1):
            left_min = min(nums[:i])
            right_min = min(nums[i + 1 : ])

            if left_min < nums[i] and right_min < nums[i]:
                sum = left_min + right_min + nums[i]
                min_sum = min(min_sum, sum)
        

        return min_sum if min_sum != float('inf') else -1     

        
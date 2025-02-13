class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_sum = sum(nums[:k])
        curr = max_sum

        for r in range(k, len(nums)):
            curr -= nums[r - k] 
            curr += nums[r]
            max_sum = max(max_sum, curr)

        return max_sum / k    

        
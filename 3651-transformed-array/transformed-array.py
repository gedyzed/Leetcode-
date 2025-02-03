class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [0 for _ in nums]
        for i, num in enumerate(nums):
            idx = num + i
            result[i] = nums[idx % n]

        return result    

        
        
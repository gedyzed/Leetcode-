class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        n, result  = len(nums), []
        for i, num in enumerate(nums):
            idx = num + i
            result.append(nums[idx % n])

        return result    

        
        
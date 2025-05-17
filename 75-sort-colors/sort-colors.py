class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        result = []
        for i in range(3):
            result.extend([i] * count[i])

        for i in range(len(nums)):
            nums[i] = result[i]

        return nums     
        

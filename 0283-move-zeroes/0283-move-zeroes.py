class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current  = 0
        for i in range(len(nums)):
            if nums[i]:
                if i != current:
                    nums[current], nums[i] = nums[i], nums[current]
                current += 1    
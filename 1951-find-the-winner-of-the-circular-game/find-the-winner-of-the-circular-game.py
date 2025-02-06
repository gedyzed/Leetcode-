class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        nums = [num for num in range(1, n + 1)]
        i = 0
        while len(nums) > 1:
            i = (i + k - 1) % len(nums)
            nums.pop(i)

        return nums[0]    

        
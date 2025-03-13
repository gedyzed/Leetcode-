class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        nums = [num for num in range(1, n + 1)]
        def winner(i):
            if len(nums) == 1: 
                return nums[0]

            i = (i + k - 1) % len(nums)
            nums.pop(i)

            return winner(i) 

        return winner(n)   

        
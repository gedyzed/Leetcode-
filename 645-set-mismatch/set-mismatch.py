class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        totalSum = int(n / 2 * (n + 1))
        currSum = sum(set(nums))
        print(totalSum, currSum)
        return [sum(nums) - currSum, totalSum - currSum]
 

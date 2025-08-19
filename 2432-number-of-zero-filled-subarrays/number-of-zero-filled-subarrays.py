class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        count = n = 0 # n -> zeros
        for i in range(len(nums)):
            if nums[i]:
                count += (n / 2) * (n + 1)
                n = 0

            if not nums[i]:
                n += 1

        count += (n / 2) * (n + 1)
        return int(count)           

        
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        s_nums = sorted([(num, i) for i, num in enumerate(nums)])
        ans = [0] * len(nums)
        ans[s_nums[0][1]] = 0
        for i in range(1, len(nums)):
            if s_nums[i][0] == s_nums[i - 1][0]:
                ans[s_nums[i][1]] = ans[s_nums[i - 1][1]]
            else:
                ans[s_nums[i][1]] = i

        return ans
            

        
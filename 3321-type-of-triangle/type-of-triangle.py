class Solution:
    def triangleType(self, nums: List[int]) -> str:

        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"

        ans = ["equilateral","isosceles", "scalene"]
        return ans[len(set(nums)) - 1]
        
        
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        n, count = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                num = nums[i] + nums[j]
                idx = bisect_left(nums, num)
                count += max(0, idx - j - 1)
                
        return count        
             
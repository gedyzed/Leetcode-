class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        res = []
        for i, nums in enumerate(grid):
            grid[i].sort()
            while limits[i] and nums:
                res.append(nums.pop())
                limits[i] -= 1

        return sum(sorted(res, reverse=True)[:k]) if len(res) >= k else sum(res)


        



          


        
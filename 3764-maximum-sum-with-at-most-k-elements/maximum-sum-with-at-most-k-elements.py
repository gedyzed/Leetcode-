class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        for i in range(len(grid)):
            grid[i].sort()
    
        res = []
        for i, nums in enumerate(grid):
            limit = limits[i]
            while limit and nums:
                res.append(nums.pop())
                limit -= 1

        return sum(sorted(res, reverse=True)[:k]) if len(res) >= k else sum(res)


        



          


        
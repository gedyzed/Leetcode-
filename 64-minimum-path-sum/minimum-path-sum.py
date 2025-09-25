class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dir = [(0, 1), (1, 0)]
        inbound = lambda r, c: 0 <= r < m and 0 <= c < n
        memo = defaultdict(int)

        def dp(row, col):
            idx = (row, col)
            if idx in memo:
                return memo[idx]
            
            if idx == (m - 1 , n - 1):
                return grid[row][col] 

            res = float("inf")
            for dr, dc in dir:
                nr, nc = row + dr, col + dc
                if inbound(nr, nc):
                    res = min(res, dp(nr, nc) + grid[row][col])
                    
            memo[idx] = res
            return res 

        return dp(0, 0) 


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        max_row = max_col = 0
        min_row, min_col = len(grid), len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    max_row = max(r, max_row)
                    max_col= max(c, max_col)

                    min_row = min(min_row, r)
                    min_col = min(min_col, c)

        r = max_row - min_row
        c = max_col - min_col
        return (r + 1) * (c + 1)            


        
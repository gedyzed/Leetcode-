class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
                 
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def inbound(row, col): 
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if inbound(new_row, new_col):
                            if not grid[new_row][new_col]:
                                ans += 1         
                        else:
                            ans += 1             

        return ans

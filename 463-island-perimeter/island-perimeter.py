class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        def dfs(row, col):
            nonlocal ans
            visited.add((row, col))


            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc 

                if inbound(new_row, new_col):
                    if (new_row, new_col) not in visited:
                        if grid[new_row][new_col]:
                            dfs(new_row, new_col) 
                        else:
                            ans += 1
                else:
                    ans += 1

                              
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def inbound(row, col): 
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()
        self.p = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    dfs(row, col)
                    return ans

        # return ans
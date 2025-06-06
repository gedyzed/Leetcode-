class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):

            area = 1
            visited.add((row, col))   
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc
                
                if inbound(new_r, new_c) and grid[new_r][new_c] and (new_r, new_c) not in visited:
                    area += dfs(new_r, new_c) 

            return area        
                    

        visited = set()
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and (row, col) not in visited:
                    area = dfs(row, col)
                    ans = max(ans, area)

        return ans            
                                   
                        
        
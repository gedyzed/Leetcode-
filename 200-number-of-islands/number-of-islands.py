class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        visited = set()
        self.islands = 0
        def dfs(row, col):
            visited.add((row, col))
            for row_range, col_range in directions: 
                new_row = row + row_range
                new_col = col + col_range
               
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    if grid[new_row][new_col] == '1':
                        dfs(new_row, new_col)
                        
                       
        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col) 
                    self.islands += 1    

        return self.islands                

                    



        
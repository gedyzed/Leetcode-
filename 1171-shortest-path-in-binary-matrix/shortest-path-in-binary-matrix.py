class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        n = len(grid)   
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = deque([(0, 0, 1)])  #(row, col, length)  
        visited = set([0, 0]) 
        while queue:
            for _ in range(len(queue)):
                row, col, length = queue.popleft()
                if row == col == n - 1:
                    return length

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if inbound(r, c) and not grid[r][c] and (r, c) not in visited:
                        queue.append((r, c, length + 1)) 
                        visited.add((r, c))  

        return -1                


            





        
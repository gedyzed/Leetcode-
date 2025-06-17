class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        time = fresh = 0
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                     queue.append((r, c))   

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if inbound(row, col) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1

            time += 1 
            
        return time if not fresh else -1    



                                    
                        



        
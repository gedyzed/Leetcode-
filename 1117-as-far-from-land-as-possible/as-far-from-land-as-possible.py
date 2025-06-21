class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        rows, cols = len(grid), len(grid[0])
        ans = [[-1] * cols for _ in range(rows)]

        queue = deque() 
        water = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    ans[r][c] = 0
                    queue.append((r, c))
                else:
                    water += 1  

        # len(queue) -> number of water
        if not water or not len(queue):
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_distance = 0
        while queue:
            row, col = queue.popleft() 
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if inbound(r, c) and ans[r][c] == -1:
                    ans[r][c] = ans[row][col] + 1
                    max_distance = max(max_distance, ans[r][c])
                    queue.append((r, c))
 
        return max_distance  

        
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['.' for _ in range(n)] for _ in range(m)]

        # Mark guards and walls
        for r, c in guards:
            grid[r][c] = 'G'
        for r, c in walls:
            grid[r][c] = 'W'

        directions = [(-1,0),(1,0),(0,-1),(0,1)] 

        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in ('G','W'):
                    if grid[nr][nc] == '.':
                        grid[nr][nc] = 'X'  # guarded
                    nr += dr
                    nc += dc

        # Count unguarded cells
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '.':
                    count += 1
        return count

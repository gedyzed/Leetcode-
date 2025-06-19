class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        def inbound(row, col):
            return (0 <= row < len(isWater) and 0 <= col < len(isWater[0]))

        rows, cols = len(isWater), len(isWater[0])
        ans = [[-1] * cols for _ in range(rows)]

        queue = deque() 
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    ans[r][c] = 0
                    queue.append((r, c))

  
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft() 
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if inbound(r, c) and ans[r][c] == -1:
                    ans[r][c] = ans[row][col] + 1
                    queue.append((r, c))

        return ans             
                      


        
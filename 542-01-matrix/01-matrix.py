class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))

        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        queue = deque()
        visited = set()

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if not mat[r][c]:
                    queue.append((r, c, 0))
                    visited.add((r, c))
            
        while queue:
            for _ in range(len(queue)):
                row, col, length = queue.popleft()
                if ans[row][col] == 0 and mat[row][col]:
                    ans[row][col] = length

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if inbound(r, c) and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c, length + 1))    

        return ans                 


        
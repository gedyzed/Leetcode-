class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        def dfs(row, col):
            image[row][col] = color
            visited.add((row, col))
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if (inbound(new_r, new_c) and
                    (new_r, new_c) not in visited and
                    image[new_r][new_c] == start_color):
                    dfs(new_r, new_c)

        start_color = image[sr][sc]
        if start_color == color:
            return image 

        visited = set()
        dfs(sr, sc)
        return image

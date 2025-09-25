class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dir = [(0, 1), (1, 0)]
        inbound = lambda r, c: 1 <= r <= m and 1 <= c <= n
        visited = set()
        memo = defaultdict(int)
        def dfs(row, col):

            idx = (row, col)
            if idx in memo:
                return memo[idx]

            if idx == (m, n):
                return 1

            count = 0
            visited.add((row, col))
            for dr, dc in dir:
                nr, nc = row + dr, col + dc
                if inbound(nr, nc):
                    count += dfs(nr, nc)

            memo[idx] = count
            return count

        return dfs(1, 1)





        
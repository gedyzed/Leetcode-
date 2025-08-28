class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)
        diagonals = defaultdict(list)
        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                diagonals[r - c].append(num)
        

        ans = [[0] * n for _ in range(n)]
        for idx in diagonals:
            nums = diagonals[idx]
            if idx < 0:
                nums.sort()
            else:
                nums.sort(reverse=True)  

            nums = nums[::-1]     
            for r in range(n):
                for c in range(n):
                    if r - c == idx:
                        ans[r][c] = nums.pop()

        return ans


        
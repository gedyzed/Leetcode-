class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        # extract diagonals
        n = len(grid)
        diagonals = defaultdict(list)
        row = defaultdict(list)
        col = defaultdict(list)

        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                diagonals[r - c].append(num)
                row[r - c].append(r)
                col[r - c].append(c)

        # create ans matrix 
        # sort the diagonals and reverse to make it suitable for pop
        # for each daigonals over certain rows and cols and check

        ans = [[0] * n for _ in range(n)]
        for idx in diagonals:
            nums = diagonals[idx]
            if idx < 0:
                nums.sort(reverse=True)
            else:
                nums.sort()       
            for r in row[idx]:
                for c in col[idx]:
                    if r - c == idx:
                        ans[r][c] = nums.pop()

        return ans


        
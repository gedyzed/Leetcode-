class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(row):

            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for col in range(n):
                if col in cols or row + col in posDgl or row - col in negDgl:
                    continue

                cols.add(col) 
                posDgl.add(row + col)  
                negDgl.add(row - col) 
                board[row][col] = "Q"

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                posDgl.remove(row + col)
                negDgl.remove(row - col)


        cols, posDgl = set(), set()
        negDgl = set()
        res = []
        board = [['.'] * n for _ in range(n)]
        backtrack(0)
        return len(res)
        
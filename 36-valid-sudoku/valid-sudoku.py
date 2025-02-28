from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def block_check(row, col):
            block_set = set()
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if board[r][c] != '.':
                        if board[r][c] in block_set:
                            return False
                        block_set.add(board[r][c])
            return True

        for row in range(len(board)):
            row_set = set()
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    if board[row][col] in row_set:
                        return False
                    row_set.add(board[row][col])


        for col in range(len(board[0])):
            col_set = set()
            for row in range(len(board)):
                if board[row][col] != '.':
                    if board[row][col] in col_set:
                        return False
                    col_set.add(board[row][col])
  

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not block_check(row, col):
                    return False

        return True
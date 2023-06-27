# Determine if a 9x9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits
# 1-9 without repetition.


class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            li = {}
            for j in range(9):
                if board[i][j] in li and board[i][j] != '.':
                    return False
                li[board[i][j]] = 1
        for i in range(9):
            li = {}
            for j in range(9):
                if board[j][i] in li and board[j][i] != '.':
                    return False
                li[board[j][i]] = 1
        for i in range(9):
            li = {}
            for j in range(9):
                x = (i % 3)*3 + j % 3
                y = (i // 3)*3 + j // 3
                if board[x][y] in li and board[x][y] != '.':
                    return False
                li[board[x][y]] = 1
        return True


a = Solution()
print(a.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

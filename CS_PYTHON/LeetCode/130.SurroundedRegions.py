# Given a 2D board containing 'X' and 'O' (the letter O), capture all
# regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that
# surrounded region.

from collections import deque

# Unfortunately, I failed to solve this problem.
# These 2 answers is leetcode's answer and they used DFS and BFS.


class Solution:
    '''
    Time complexity : O(MXN)
    Space complexity : O(1)

    First, check the four border of the matrix. If there is a element is
    'O', alter it and all its neighbor 'O' elements to 'N'.

    Then ,alter all the 'O' to 'X'

    At last,alter all the 'N' to 'O'

    example:

    X X X X           X X X X             X X X X
    X X O X  ->       X X O X    ->       X X X X
    X O X X           X N X X             X O X X
    X O X X           X N X X             X O X X

    '''

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return

        # queue for bfs
        q = deque()

        # start from the boarder and replace all O to N
        # put all the boarder value into queue.
        for r in range(R):
            q.append((r, 0))
            q.append((r, C-1))

        for c in range(C):
            q.append((0, c))
            q.append((R-1, c))

        while q:
            r, c = q.popleft()
            if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
                # modify the value from O to N
                board[r][c] = "N"
                # append the surrouding cells to queue.
                q.append((r, c+1))
                q.append((r, c-1))
                q.append((r-1, c))
                q.append((r+1, c))

        # replace all the O to X, then replace all the N to O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"


class Solution1:

    '''
    recursion, dfs
    '''

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return

        # start from the boarder and replace all O to N
        # put all the boarder value into queue.
        for r in range(R):
            self.dfs(board, r, 0, R, C)
            self.dfs(board, r, C-1, R, C)

        for c in range(C):
            self.dfs(board, 0, c, R, C)
            self.dfs(board, R-1, c, R, C)

        # replace all the O to X, then replace all the N to O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"

    def dfs(self, board, r, c, R, C):
        if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
            board[r][c] = "N"
            self.dfs(board, r, c+1, R, C)
            self.dfs(board, r, c-1, R, C)
            self.dfs(board, r-1, c, R, C)
            self.dfs(board, r+1, c, R, C)


a = Solution()
a.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])

